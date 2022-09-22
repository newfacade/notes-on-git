#!/usr/bin/env python
# coding: utf-8

# # 撤销操作
# 
# ```{note}
# 在任何一个阶段，你都有可能想要撤销某些操作。这里，我们将会学习几个撤销你所做修改的基本工具。注意，有些撤销操作是不可逆的！
# ```

# ## 覆盖提交
# 
# 有时候我们提交完了才发现漏掉了几个文件没有添加，或者提交信息写错了。此时，可以运行带有 `--amend` 选项的的提交命令来重新提交。例如，你提交后发现忘记了暂存某些需要的修改，可以像下面这样操作：
# 
# ```
# $ git commit -m 'initial commit'
# $ git add forgotten_file
# $ git commit --amend
# ```
# 
# 最终你只会有一个提交 - 第二次提交将代替第一次提交的结果。

# ## 取消暂存的文件
# 
# 通过一个例子来说明：假如你已经修改了两个文件并且想要将它们作为两次独立的修改提交，但确意外地输入 `git add *` 暂存了它们两个。如何取消暂存两个中的一个呢？`git status` 命令提示了你：
# 
# ```
# $ git add *
# $ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     renamed:    README.md -> README
#     modified:   CONTRIBUTING.md
# ```
# 
# 在 Changes to be committed 文字正下方，提示使用 `git reset HEAD <file>...` 来取消暂存。所以，我们可以这样来取消暂存 CONTRIBUTING.md 文件：
# 
# ```
# $ git reset HEAD CONTRIBUTING.md
# Unstaged changes after reset:
# M	CONTRIBUTING.md
# $ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     renamed:    README.md -> README
# 
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
# 
#     modified:   CONTRIBUTING.md
# ```
# 
# 现在，CONTRIBUTING.md 已经是修改未暂存的状态了。
# 
# ```{caution}
# `git reset` 确实是一个危险的命令，如果加上了 `--hard` 选项则更是如此。然而在上述场景中，工作目录中的文件尚未修改，因此相对安全一些。
# ```

# ## 撤销对文件的修改
# 
# 如果你并不想保留对 CONTRIBUTING.md 文件的修改怎么办？你该如何方便地撤销修改 - 将它还原成上次提交时的样子（或者刚克隆完的样子，或者刚把它放入工作目录的样子）？`git status` 也告诉了你应该如何做。上个例子未暂存区域是这样：
# 
# ```
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
# 
#     modified:   CONTRIBUTING.md
# ```
# 
# 它非常清楚地告诉了你如何撤销之前的修改：
# 
# ```
# $ git checkout -- CONTRIBUTING.md
# $ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     renamed:    README.md -> README
# ```
# 
# 可以看到那些修改已经被撤销了。
# 
# ```{warning}
# 请务必记得 `git checkout -- <file>` 是一个危险的命令。你对那个文件在本地的任何修改都会消失 - Git 会用最近提交的版本覆盖掉它。<br>
# 记住，在 Git 中任何 **已提交** 的东西几乎总是可以恢复的。然而，任何你未提交的东西丢失后很可能再也找不到了。
# ```

# ## 回退
# 
# `git reset` 命令是在更改 HEAD 的指向，使其指向不同的 commit。
# 
# 要想用好 reset 命令，必须理解它的三个参数：--soft，--mixed（默认）和 --hard。
# 
# 1. soft 参数是指将本地仓库区回退到指定版本，但是暂存区和工作区保持不变。
# 2. mixed 参数将本地仓库区和暂存区回退到指定版本，但是工作区保持不变。
# 3. hard 参数将本地仓库区、暂存区和工作区都回退到指定版本。
# 
# ```{warning}
# 工作区有未提交的代码时不要使用 --hard 参数，因为工作区会回退，你没有提交的代码就再也找不回了！
# ```
# 
# 例子：
# 
# 回退到上一个版本：
# 
# ```
# $ git reset HEAD^
# ```
# 
# 回退到指定版本（这里 commit_id 可以通过 `git log` 查看，这里使用了 commit_id 的前 4 个字母）：
# 
# ```
# $ git --soft reset 052e
# ```
# 
# 强行回退到上上上个版本：
# 
# ```
# $ git reset --hard HEAD~3
# ```

# In[ ]:




