#!/usr/bin/env python
# coding: utf-8

# # 分支管理
# 
# `git branch` 命令不止可以创建和删除分支。如果不加任何参数运行，会得到当前所有分支的一个列表：
# 
# ```
# $ git branch
#   iss53
# * master
#   testing
# ```
# 
# 注意 master 分支前的 * 字符：它表示现在检出那个分支。这意味着如果在这时候提交，master 分支将会随着新的工作向前移动。如果要查看每个分支的最后一个提交，可以运行 `git branch -v` 命令：
# 
# ```
# $ git branch -v
#   iss53   93b412c fix javascript issue
# * master  7a98805 Merge branch 'iss53'
#   testing 782fd34 add scott to the author list in the readmes
# ```
# 
# --merged 和 --no-merged 这两个有用的选项可以过滤这个列表中已经合并或尚未合并到当前分支的分支：
# 
# ```
# $ git branch --merged
#   iss53
# * master
# ```
# 
# 因为之前已经合并了 iss53 分支。
# 
# ```
# $ git branch --no-merged
#   testing
# ```
# 
# 因为 testing 分支包含了还未合并的工作。

# In[ ]:




