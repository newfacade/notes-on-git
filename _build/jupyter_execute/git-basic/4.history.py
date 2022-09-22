#!/usr/bin/env python
# coding: utf-8

# # 查看提交历史
# 
# ```{note}
# 在提交若干更新，又或者克隆了某个项目之后，你也许想回顾下提交历史。完成这个任务最简单而有效的的工具是 `git log` 命令。
# ```
# 
# 我们使用一个非常简单的 simplegit 项目作为示例，先获取该项目：
# 
# ```
# $ git clone https://github.com/schacon/simplegit-progit
# ```
# 
# 当你在此项目中运行 `git log` 命令时，可以看到下面的输出：
# 
# ```
# $ git log
# commit ca82a6dff817ec66f44342007202690a93763949
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Mon Mar 17 21:52:11 2008 -0700
# 
#     changed the version number
# 
# commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Sat Mar 15 16:40:33 2008 -0700
# 
#     removed unnecessary test
# 
# commit a11bef06a3f659402fe7563abf99ad00de2209e6
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Sat Mar 15 10:31:28 2008 -0700
# 
#     first commit
# ```
# 
# 不传入任何参数的默认情况下，`git log` 按时间先后顺序列出所有的提交、最近的排在最上面。这个命令会列出每个提交的 SHA-1 校验和、作者的名字和电子邮件地址、提交时间以及提交说明。
# 
# `git log` 有许多选项可以帮你搜寻提交。其中一个很有用的选项是 `--stat`，它会显示每次提交的简略统计信息：
# 
# ```
# $ git log --stat
# commit ca82a6dff817ec66f44342007202690a93763949
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Mon Mar 17 21:52:11 2008 -0700
# 
#     changed the version number
# 
#  Rakefile | 2 +-
#  1 file changed, 1 insertion(+), 1 deletion(-)
# 
# commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Sat Mar 15 16:40:33 2008 -0700
# 
#     removed unnecessary test
# 
#  lib/simplegit.rb | 5 -----
#  1 file changed, 5 deletions(-)
# 
# commit a11bef06a3f659402fe7563abf99ad00de2209e6
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Sat Mar 15 10:31:28 2008 -0700
# 
#     first commit
# 
#  README           |  6 ++++++
#  Rakefile         | 23 +++++++++++++++++++++++
#  lib/simplegit.rb | 25 +++++++++++++++++++++++++
#  3 files changed, 54 insertions(+)
# ```
# 
# 也可以限制显示的日志条目数，例如 `-2` 选项只显示最近的两次提交：
# 
# ```
# $ git log -2
# commit ca82a6dff817ec66f44342007202690a93763949
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Mon Mar 17 21:52:11 2008 -0700
# 
#     changed the version number
# 
# commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
# Author: Scott Chacon <schacon@gee-mail.com>
# Date:   Sat Mar 15 16:40:33 2008 -0700
# 
#     removed unnecessary test
# ```

# In[ ]:




