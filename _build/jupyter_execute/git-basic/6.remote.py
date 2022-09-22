#!/usr/bin/env python
# coding: utf-8

# # 远程仓库的使用
# 
# ```{note}
# 为了能在任意 Git 项目上协作，你需要知道如何管理自己的远程仓库。远程仓库是指托管在因特网或其他网络中的你的项目的版本库。<br>
# 你可以有好几个远程仓库，通常有些仓库对你只读，有些可以读写。与他人协助涉及管理远程仓库以及根据需要推送或拉取数据。
# ```

# ## 查看远程仓库
# 
# 如果你想查看已经配置的远程仓库服务器，可以运行 `git remote` 命令。<br>
# 如果你已经克隆了自己的仓库，那么至少应该能看到 origin - 这是 Git 给你克隆的仓库服务器的默认名字：
# 
# ```
# $ git clone https://github.com/schacon/ticgit
# Cloning into 'ticgit'...
# remote: Reusing existing pack: 1857, done.
# remote: Total 1857 (delta 0), reused 0 (delta 0)
# Receiving objects: 100% (1857/1857), 374.35 KiB | 268.00 KiB/s, done.
# Resolving deltas: 100% (772/772), done.
# Checking connectivity... done.
# $ cd ticgit
# $ git remote
# origin
# ```
# 
# You can also specify `-v`, which shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote:
# 
# ```
# $ git remote -v
# origin	https://github.com/schacon/ticgit (fetch)
# origin	https://github.com/schacon/ticgit (push)
# ```
# 
# 如果你的远程仓库不止一个，该命令会将它们全部列出：
# 
# ```
# $ cd grit
# $ git remote -v
# bakkdoor  https://github.com/bakkdoor/grit (fetch)
# bakkdoor  https://github.com/bakkdoor/grit (push)
# cho45     https://github.com/cho45/grit (fetch)
# cho45     https://github.com/cho45/grit (push)
# defunkt   https://github.com/defunkt/grit (fetch)
# defunkt   https://github.com/defunkt/grit (push)
# koke      git://github.com/koke/grit.git (fetch)
# koke      git://github.com/koke/grit.git (push)
# origin    git@github.com:mojombo/grit.git (fetch)
# origin    git@github.com:mojombo/grit.git (push)
# ```

# ## 添加远程仓库
# 
# 前面已经提到过 `git clone` 命令会自动添加远程仓库，这里将告诉你如何自己来添加它。运行 `git remote add <shortname> <url>` 会添加一个新的远程 Git 仓库，同时指定其简写：
# 
# ```
# $ git remote
# origin
# $ git remote add pb https://github.com/paulboone/ticgit
# $ git remote -v
# origin	https://github.com/schacon/ticgit (fetch)
# origin	https://github.com/schacon/ticgit (push)
# pb	https://github.com/paulboone/ticgit (fetch)
# pb	https://github.com/paulboone/ticgit (push)
# ```
# 
# 现在你可以在命令行中使用字符 pb 来替代整个 URL。例如，如果你想拉取 Paul 的仓库中有但你没有的信息，可以运行 `git fetch pb`：
# 
# ```
# $ git fetch pb
# remote: Counting objects: 43, done.
# remote: Compressing objects: 100% (36/36), done.
# remote: Total 43 (delta 10), reused 31 (delta 5)
# Unpacking objects: 100% (43/43), done.
# From https://github.com/paulboone/ticgit
#  * [new branch]      master     -> pb/master
#  * [new branch]      ticgit     -> pb/ticgit
# ```
# 
# 现在 Paul 的 master 分支可以在本地通过 pb/master 访问到 - 你可以将它合并到自己的某个分支中，或者如果你想要查看它的话，可以检出一个指向该点的本地分支。

# ## 从远程仓库中 Fetching and Pulling
# 
# 就如刚才所见，从远程仓库获取数据，可以执行：
# 
# ```
# $ git fetch <remote>
# ```
# 
# 这个命令会访问远程仓库，从中拉取所有你还没有得数据。执行完成后，你将会拥有那个远程仓库中所有分支的引用，可以随时合并或查看。
# 
# ```{caution}
# 注意 `git fetch` 命令只会将数据下载到你的本地仓库 - 它并不会自动合并或修改你当前的工作。当你准备好时你必须手动将其合并入你的工作。
# ```
# 
# 如果你的当前分支设置了跟踪远程分支（阅读下一章了解更多信息），那么可以用 `git pull` 命令来自动抓取后合并该远程分支到当前分支。这或许是更加简单舒服的工作流程。默认情况下，`git clone` 命令会自动设置本地 master 分支跟踪克隆的远程仓库的 master 分支。

# ## 推送到远程仓库
# 
# 当你想分享你的项目时，必须将其推送到上游。这个命令是 `git push <remote> <branch>`。当你想要将 master 分支推送到 origin 服务器时：
# 
# ```
# $ git push origin master
# ```
# 
# 只有当你有所克隆服务器的写入权限，并且之前没有人推送过时，这条命令才会生效。<br>
# 当你和其他人在同一时间克隆，他们先推送到上游然后你再推送到上游，你的推送就会毫无疑问被拒绝。你必须先抓取他们的工作并将其合并进你的工作后才能推送。

# ## 查看某个远程仓库
# 
# 如果想要查看某一个远程仓库的更多信息，可以使用 `git remote show <remote>` 命令：
# 
# ```
# $ git remote show origin
# * remote origin
#   URL: https://github.com/my-org/complex-project
#   Fetch URL: https://github.com/my-org/complex-project
#   Push  URL: https://github.com/my-org/complex-project
#   HEAD branch: master
#   Remote branches:
#     master                           tracked
#     dev-branch                       tracked
#     markdown-strip                   tracked
#     issue-43                         new (next fetch will store in remotes/origin)
#     issue-45                         new (next fetch will store in remotes/origin)
#     refs/remotes/origin/issue-11     stale (use 'git remote prune' to remove)
#   Local branches configured for 'git pull':
#     dev-branch merges with remote dev-branch
#     master     merges with remote master
#   Local refs configured for 'git push':
#     dev-branch                     pushes to dev-branch                     (up to date)
#     markdown-strip                 pushes to markdown-strip                 (up to date)
#     master                         pushes to master                         (up to date)
# ```
# 
# 我们从上往下看，它列出了远程仓库的 URL，并告诉你正处于 master 分支。<br>
# Remote branches 列出了所有跟踪分支，并列出了哪些分支不在你的本地，哪些分支已经在服务器上移除了。<br>
# Local branches configured for 'git pull' 列出了当你执行 `git pull` 时哪些本地分支（需已抓取，即 pulled down）可以与它跟踪的远程分支合并。这里，如果运行 `git pull`，就会抓取（fetch）所有的远程引用，然后将远程 master 分支合并到本地 master 分支。<br>
# Local refs configured for 'git push' 列出了当你在特定分支上执行 `git push` 会自动推送到哪一个远程分支。

# ## 远程仓库重命名和移除
# 
# 可以运行 `git remote rename` 来修改远程仓库的简写名。比如说，想要将 pb 重命名为 paul：
# 
# ```
# $ git remote rename pb paul
# $ git remote
# origin
# paul
# ```
# 
# 如果因为一些原因想要移除一个远程仓库，可以使用 `git remote remove` 或 `git remote rm`：
# 
# ```
# $ git remote remove paul
# $ git remote
# origin
# ```
# 
# 一旦你使用这种方式删除了一个远程仓库, all remote-tracking branches and configuration settings associated with that remote are also deleted.

# In[ ]:




