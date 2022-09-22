#!/usr/bin/env python
# coding: utf-8

# # 分支合并
# 
# ```{note}
# 本节我们通过一个例子来理解分支合并。
# ```
# 
# ## 分叉
# 首先，我们假设你正在你的项目上工作，并且在 master 分支上已经有了一些提交。
# 
# ![](../images/merge1.png)
# 
# 现在，你已经决定要解决你的公司使用的问题追踪系统的 #53 问题。想要新建一个分支并同时切换到那个分支上：
# 
# ```
# git checkout -b iss53
# ```
# 
# ![](../images/merge2.png)
# 
# 你继续在 #53 问题上工作，并且做了一些提交。在此过程中，iss53 分支在不断向前推进。
# 
# ```
# $ vim index.html
# $ git commit -a -m 'added a new footer [issue 53]'
# ```
# 
# ![](../images/merge3.png)
# 
# 现在你接到一个电话，有个紧急问题等待你来解决。有了 Git 的帮助，你不必把这个紧急问题和 iss53 的修改混在一起，也不需要花大力气来还原关于 #53 问题的修改然后再添加关于这个紧急问题的修改。你要做的仅仅是切换回 master 分支。
# 
# 但是，在这么做之前，**要留意你的工作目录和暂存区里那些还没被提交的修改，它可能会和你即将检出的分支产生冲突从而阻止 Git 切换分支**。最好的方法是，在你切换分支之前，保持一个干净的状态（可以创建新的提交，也可以通过暂存（stashing）和修补提交（commit amending）绕过这个问题）。
# 
# ```{note}
# 有时，当你在项目的一部分上已经工作一段时间后，所有东西都进入了混乱的状态，而这时候你想要切换到另一个分支做一点别的事情。问题是，你不想仅仅因为过会儿回到这一点而为做一半的工作创建一次提交。针对这个问题的答案就是 `git stash` 命令。<br>
# 贮藏（stash）会处理工作目录的脏的状态 - 即跟踪文件的修改和暂存的改动 - 然后将未完成的修改保存到一个栈上，而你可以在任何时候重新应用这些改动（甚至在不同的分支上）。
# ```
# 
# 现在，我们假设你已经把你的修改全部提交了，这时，你可以切换回 master 分支了：
# 
# ```
# $ git checkout master
# Switched to branch 'master'
# ```
# 
# 接下来，你要修复这个紧急问题。我们来建立一个 hotfix 分支，在该分支上工作直到问题解决：
# 
# ```
# $ git checkout -b hotfix
# Switched to a new branch 'hotfix'
# $ vim index.html
# $ git commit -a -m 'fixed the broken email address'
# [hotfix 1fb7853] fixed the broken email address
#  1 file changed, 2 insertions(+)
# ```
# 
# ![](../images/merge4.png)
# 
# 你可以运行你的测试，确保你的修改时正确的，然后将 hotfix 分支合并回你的 master 分支来部署到线上。你可以使用 `git merge` 命令达到上述目的：
# 
# ```
# $ git checkout master
# $ git merge hotfix
# Updating f42c576..3a0874c
# Fast-forward
#  index.html | 2 ++
#  1 file changed, 2 insertions(+)
# ```
# 
# 在合并的时候，你应该注意到了“快进（fast-forward）”这个词。因为合并是简单地将指针向前推进，合并操作没有需要解决的分歧 - 这就叫快进。
# 
# ![](../images/merge5.png)
# 
# 这个紧急问题的解决方案发布之后，你准备回到 #53 问题的修复中。你应该先删除 hotfix 分支 - 你已经不再需要它，master 分支已指向同一位置。你可以使用带 `git branch -d` 来删除分支：
# 
# ```
# $ git branch -d hotfix
# Deleted branch hotfix (3a0874c).
# ```
# 
# 切换回 iss53 分支：
# 
# ```
# $ git checkout iss53
# Switched to branch "iss53"
# $ vim index.html
# $ git commit -a -m 'finished the new footer [issue 53]'
# [iss53 ad82d7a] finished the new footer [issue 53]
# 1 file changed, 1 insertion(+)
# ```
# 
# ![](../images/merge6.png)
# 
# 注意，你在 hotfix 分支上所做的工作并没有包含到 iss53 分支中。

# ## 合并
# 
# 假设你已经修正了 #53 问题，并且打算将你的工作合并入 master 分支：
# 
# ```
# $ git checkout master
# Switched to branch 'master'
# $ git merge iss53
# Merge made by the 'recursive' strategy.
# index.html |    1 +
# 1 file changed, 1 insertion(+)
# ```
# 
# 这和你之前合并 hotfix 分支的时候看起来有点不一样。在这种情况下，在这种情况下，你的开发历史从一个更早的地方开始分叉开来（diverged）。出现这种情况的时候，Git 会使用两个分支所指的快照（C4 和 C5）以及这两个分支的共同祖先（C2），做一个简单的 **三方合并** 。
# 
# ![](../images/merge7.png)
# 
# 和之前将分支指针向前推进所不同的是，Git 将此次三方合并的结果 **做了一个新的快照并且自动创建一个新的提交指向它** 。这个被称作一次合并提交，它的特别之处在于他有不止一个父提交。
# 
# ![](../images/merge8.png)
# 
# 既然你的修改已经合并进来了，就不再需要 iss53 分支了：
# 
# ```
# $ git branch -d iss53
# ```

# ## 遇到冲突时的分支合并
# 
# 有时候合并操作不会如此顺利。如果你在不同的分支中，**对同一个文件的同一个部分进行了不同的修改** ，Git 就没法干净的合并它们。比如说 #53 的修改和 hotfix 的修改涉及到同一文件的同一处：
# 
# ```
# $ git merge iss53
# Auto-merging index.html
# CONFLICT (content): Merge conflict in index.html
# Automatic merge failed; fix conflicts and then commit the result.
# ```
# 
# 此时 Git 做了合并，但是没有自动地创建一个新的合并提交。Git 会暂停下来，等待你去解决合并产生的冲突。你可以使用 `git status` 命令来查看那些因包含冲突而处于未合并（unmerged）状态的文件：
# 
# ```
# $ git status
# On branch master
# You have unmerged paths.
#   (fix conflicts and run "git commit")
# 
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
# 
#     both modified:      index.html
# 
# no changes added to commit (use "git add" and/or "git commit -a")
# ```
# 
# Git 会在有冲突的文件中加入标准的冲突解决标记，这样你可以打开这些包含冲突的文件然后手动解决冲突。出现冲突的文件会包含一些特殊区段，看起来像下面这个样子：
# 
# ```
# <<<<<<< HEAD:index.html
# <div id="footer">contact : email.support@github.com</div>
# =======
# <div id="footer">
#  please contact us at support@github.com
# </div>
# >>>>>>> iss53:index.html
# ```
# 
# 这表示 HEAD 所指示的版本（也就是 master 分支所在的位置，因为之前已检出）在这个区段的上半部分（ ======= 的上半部分），而 iss53 分支所指示的版本在 ======= 的下半部分。为了解决冲突，你必须选择使用由 ======= 分割的两部分中的一个，或者你也可以自行合并这些内容。例如，你可以通过把这段内容换成下面的样子来解决冲突：
# 
# ```
# <div id="footer">
# please contact us at email.support@github.com
# </div>
# ```
# 
# 上述的冲突解决方案仅保留了其中一个分支的修改，并且 <<<<<<< , ======= , 和 >>>>>>> 这些被完全删除了。**在你解决了所有文件里的冲突之后，对每个文件使用 `git add` 命令来将其标记为冲突已解决。** 一旦暂存这些原本有冲突的文件，Git 就会将它们标记为冲突已解决。
# 
# 你可以再次使用 `git status` 来确认所有合并冲突都已被解决：
# 
# ```
# $ git status
# On branch master
# All conflicts fixed but you are still merging.
#   (use "git commit" to conclude merge)
# 
# Changes to be committed:
# 
#     modified:   index.html
# ```
# 
# 如果你对结果感到满意，并且确定之前有冲突的文件都已经暂存，这时你可以使用 `git commit` 来完成合并并提交。

# In[ ]:




