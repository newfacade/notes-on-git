#!/usr/bin/env python
# coding: utf-8

# # 分支简介
# 
# ```{note}
# Git 保存的不是文件的变化或者差异，而是一系列不同时刻的快照。
# ```
# 
# 在进行提交操作时，Git 会保存一个提交对象（commit object）。该提交对象包含一个指向暂存内容的指针，此外还包含作者的姓名和邮箱、提交时输入的信息以及指向它的父对象的指针。首次提交时没有父对象，普通提交有一个父对象，而由多个分支合并产生的提交对象有多个父对象。
# 
# 例子：假设现在我们有一个工作目录，里面包含三个将要被暂存和提交的文件。暂存操作会为每个文件计算校验和（SHA-1 哈希算法），然后把当前版本的文件快照保存到 Git 仓库中（Git 使用 blob 对象来保存它们），最终将校验和加入暂存区等待提交：
# 
# ```
# $ git add README test.rb LICENSE
# $ git commit -m 'The initial commit of my project'
# ```
# 
# 当使用 `git commit` 进行提交操作时，Git 会先计算每个子目录（本例中只有项目根目录）的校验和，然后再 Git 仓库中这些校验和保存为树对象。随后，Git 便会创建一个提交对象，它除了包含上面提到的那些信息外，还包含指向这个树对象的指针。
# 
# 现在，Git 仓库中有5个对象：3个 blob 对象（保存着文件快照）、一个树对象（记录着目录结构和 blob 对象索引）以及一个提交对象（包含着指向前述树对象的指针和所有提交信息）。
# 
# ![branch](../images/branch1.png)
# 
# 做些修改后再次提交，那么这次产生的提交对象会包含一个指向上一个提交对象（父对象）的指针。
# 
# ![](../images/branch2.png)
# 
# **Git 的分支，其实本质上仅仅是指向提交对象的可变指针**。Git 的默认分支名是 master。在多次提交操作之后，你其实已经有一个指向最后那个提交对象的 master 分支。master 分支会在每次提交时自动向前移动。
# 
# ![](../images/branch3.png)

# ## 分支创建
# 
# Git 是怎么创建新分支的呢？很简单，它只是为你创建了一个可以移动的新的指针。比如，创建 testing 分支，需要使用 `git branch` 命令：
# 
# ```
# $ git branch testing
# ```
# 
# 这会在当前的提交对象上创建一个指针。
# 
# ![](../images/branch4.png)
# 
# 那么，Git 又是怎么知道当前在哪一个分支上呢？也很简单，它有名为 HEAD 的特殊指针，它指向当前所在的本地分支（将 HEAD 想象成当前分支的别名）。在本例中，你仍在 master 分支上，因为 `git branch` 命令仅仅创建一个新分支，并不会自动切换到新分支中去。
# 
# ![](../images/branch5.png)
# 
# 可以使用 `git log --oneline --decorate` 查看各个分支当前所指的对象（提供这一功能的参数是 --decorate，而 --oneline 会将每个提交放在一行显示）：
# 
# ```
# $ git log --oneline --decorate
# f30ab (HEAD -> master, testing) add feature #32 - ability to add new formats to the central interface
# 34ac2 Fixed bug #1328 - stack overflow under certain conditions
# 98ca9 The initial commit of my project
# ```
# 
# 正如你所见，当前 master 和 testing 分支均指向校验和以 f30ab 开头的提交对象。

# ## 分支切换
# 
# 要切换到一个已存在的分支，需要使用 `git checkout` 命令。我们现在切换到新创建的 testing 分支中去：
# 
# ```
# git checkout testing
# ```
# 
# 这样 HEAD 就指向 testing 分支了。
# 
# ![](../images/branch6.png)
# 
# 现在我们做些修改，再提交一次：
# 
# ![](../images/branch7.png)
# 
# 如图所示，testing 分支向前移动了，但是 master 分支却没有。我们再切换回 master 看看：
# 
# ```
# git checkout master
# ```
# 
# ![](../images/branch8.png)
# 
# 这条命令做了两件事：
# 
# 1. 使 HEAD 指回 master 分支
# 2. 将工作目录恢复成 master 分支所指向的快照内容
# 
# 我们不妨再稍稍做些修改并提交：
# 
# ```
# $ vim test.rb
# $ git commit -a -m 'made other changes'
# ```
# 
# 现在，这个项目提交历史已经产生了 **分叉**。上述两次改动针对的是不同分支：你可以在不同分支间不断地来回切换和工作，并在时机成熟时将它们合并起来。
# 
# ![](../images/branch9.png)
# 
# 你可以简单地使用 `git log` 命令查看分叉历史：
# 
# ```
# $ git log --oneline --decorate --graph --all
# * c2b9e (HEAD, master) made other changes
# | * 87ab2 (testing) made a change
# |/
# * f30ab add feature #32 - ability to add new formats to the
# * 34ac2 fixed bug #1328 - stack overflow under certain conditions
# * 98ca9 initial commit of my project
# ```
# 
# ```{tip}
# 通常我们会在创建一个新分支后立即切换过去，这可以用 `git checkout -b <newbranchname>` 一条命令搞定。
# ```

# In[ ]:




