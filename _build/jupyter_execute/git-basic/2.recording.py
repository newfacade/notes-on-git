#!/usr/bin/env python
# coding: utf-8

# # 记录每次更新到仓库
# 
# 现在，我们的机器上有了一个真实项目的 Git 仓库，并从这个仓库中检出了所有文件的工作副本。通常，你会对这些文件做些修改，每当完成了一个阶段的目标，想要记录下它时，就将它提交到仓库。
# 
# 你工作目录下的每一个文件都不外乎两种状态：
# 
# 1. 已跟踪
#     已跟踪的文件是指那些被纳入了版本控制的文件，在工作一段时间后，它们的状态可能是 **未修改**，**已修改**或**已放入暂存区**。简而言之，已跟踪的文件就是 Git 已经知道的文件。
# 2. 未跟踪
#     工作目录中除了已跟踪文件就是未跟踪文件。
#     
# 初次克隆某个仓库的时候，工作目录中所有的文件都是已跟踪文件，并处于未修改状态，因为 Git 刚刚检出它们，而你尚未编辑过它们。<br>
# 编辑某些文件之后，Git 将它们标记为已修改文件。<br>
# 在工作中，你可以选择性地将这些修改过的文件放入暂存区，然后提交所有已暂存的修改，如此反复。
# 
# ![life](../images/lifecycle.png)

# ## 检查文件状态
# 
# 可以使用 `git status` 命令查看哪些文件处于什么状态，克隆仓库后立刻使用此命令：
# 
# ```
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# nothing to commit, working directory clean
# ```
# 
# 工作目录干净，换句话说，所有已跟踪文件在上次提交后都未被更改过。<br>
# 上面的信息还表明，当前目录下没有任何处于未跟踪状态的新文件。<br>
# 最后，该命令显示了当前所在分支，分支名为 master，并且这个分支同远程服务器上对应的分支没有偏离。
# 
# 现在，让我们在项目下新建一个 README 文件：
# 
# ```
# $ echo 'My Project' > README
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
# 
#     README
# 
# nothing added to commit but untracked files present (use "git add" to track)
# ```
# 
# 从中可以看到新建的 README 文件出现在 Untracked files 下面。

# ## 跟踪新文件
# 
# 使用 `git add` 开始跟踪一个文件：
# 
# ```
# $ git add README
# ```
# 
# 此时再运行 `git status`，会看到 README 文件已被跟踪，并处于**暂存**状态：
# 
# ```
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
# 
#     new file:   README
# ```
# 
# `git add` 命令使用文件或目录的路径作为参数；如果参数是目录的路径，该命令将递归地跟踪该目录下的所有文件。

# ## 暂存已修改的文件
# 
# 如果你修改了一个名为 CONTRIBUTING.md 的已跟踪文件，然后运行 `git status`：
# 
# ```
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     new file:   README
# 
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
# 
#     modified:   CONTRIBUTING.md
# ```
# 
# 文件 CONTRIBUTING.md 出现在 Changes not staged for commit 这行下面。要暂存这次更新，需要运行 `git add` 命令。这是一个多功能命令，可以用它：
# 
# * 开始跟踪新文件
# * 把已跟踪文件放到暂存区
# * 合并时把有冲突的文件标记为已解决状态
# 
# ```{tip}
# 将 `git add` 这个命令理解为“精确地将内容添加到下一次提交中”要更加合适。
# ```
# 
# 现在使用 `git add` 将放到暂存区：
# 
# ```
# $ git add CONTRIBUTING.md
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     new file:   README
#     modified:   CONTRIBUTING.md
# ```
# 
# 现在两个文件都已暂存，下次提交时就会一并记录到仓库。假设此时，你想在 CONTRIBUTING.md 里再加条注释，重新编辑存盘后运行 `git status`：
# 
# ```
# $ vim CONTRIBUTING.md
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     new file:   README
#     modified:   CONTRIBUTING.md
# 
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
# 
#     modified:   CONTRIBUTING.md
# ```
# 
# 现在 CONTRIBUTING.md 同时出现在暂存区和非暂存区？实际上，Git 只不过暂存了你运行 `git add` 命令时的版本，而不是在工作目录中的当前版本！所以运行了 `git add` 之后又做了修订的文件，需要重新运行 `git add` 把最新版本重新暂存起来：
# 
# ```
# $ git add CONTRIBUTING.md
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     new file:   README
#     modified:   CONTRIBUTING.md
# ```

# ## 提交更新
# 
# 现在的暂存区已经准备就绪，可以提交了。在此之前，请务必确认还有什么已经修改或新建的文件还没有 `git add` 过。所以每次提交前，先用 `git status` 看下，确认后再提交：
# 
# ```
# $ git commit -m "Story 182: Fix benchmarks for speed"
# [master 463dc4f] Story 182: Fix benchmarks for speed
#  2 files changed, 2 insertions(+)
#  create mode 100644 README
# ```
# 
# 其中 -m 选项后的是提交说明。好，现在你已经完成了第一个提交！可以看到，提交后它会告诉你，当前是在哪个分支（master）提交的，本次提交的完整 SHA-1 校验和是什么（463dc4f），以及在本次提交中，有多少文件修订过，多少行添加和删改过。
# 
# ```{tip}
# 每一次运行提交操作，都是对你项目作一次快照，以后可以回到这个状态，或者进行比较。
# ```
# 
# Git 还提供了一个跳过使用暂存区域的方式，只要在提交时给 `git commit` 加上 `-a` 选项，Git 就会自动把所有**已跟踪**过的文件暂存起来一并提交，从而跳过 `git add` 步骤：
# 
# ```
# $ git commit -a -m 'added new benchmarks'
# [master 83e38c7] added new benchmarks
#  1 file changed, 5 insertions(+), 0 deletions(-)
# ```

# ## 移除文件
# 
# 要从 Git 中移除某个文件，必须要从**暂存区**移除，然后再提交。可以用 `git rm` 命令完成此项工作，它会**连带从工作目录中删除文件**，这样以后就不会出现在未跟踪清单中了。
# 
# 如果只是简单地从工作目录中手工删除文件，运行 `git status` 就会在 Changes not staged for commit 部分看到：
# 
# ```
# $ rm PROJECTS.md
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes not staged for commit:
#   (use "git add/rm <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
# 
#         deleted:    PROJECTS.md
# 
# no changes added to commit (use "git add" and/or "git commit -a")
# ```
# 
# 需要使用 `git rm` 在暂存区移除文件：
# 
# ```
# $ git rm PROJECTS.md
# rm 'PROJECTS.md'
# $ git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
# 
#     deleted:    PROJECTS.md
# ```
# 
# 下次提交时，该文件就不会纳入版本管理了。
# 
# 如果要删除之前**修改过或已放到暂存区**的文件，则必须使用强制删除选项 `-f`：
# 
# ```
# $ git rm -f README
# ```
# 
# 如果我们想把文件从 Git 仓库中删除（亦即从暂存区移除），但仍希望保存在当前工作目录中，需要使用 `--cached` 选项：
# 
# ```
# $ git rm --cached README
# ```

# ## 移动文件
# 
# Git 并不显式跟踪文件移动操作。要在 Git 中对文件改名，可以这么做：
# 
# ```
# $ git mv file_from file_to
# ```
# 
# 其实，运行 `git mv` 就相当于运行了下面三条命令：
# 
# ```
# $ mv file_from file_to
# $ git rm file_from
# $ git add file_to
# ```

# In[ ]:




