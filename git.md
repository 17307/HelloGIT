#   -   git
##  常用
-   git init 将目录变成git管理目录
-   git add file  保存文件到暂存区
-   git commit -m "文件修改说明"  提交文件到分支
-   git status  查看仓库当前的状态
-   git diff   查看当前版本和上一版本的区别
-   git log  查看历史记录
-   git reset -hard HEAD^  版本回退到上一个版本（也可以将暂存区的修改退回到工作区）
-   git reset -hard id   版本回退到commit id对应的版本
-   git checkout --file  撤销在工作区的修改
-   git rm file  删除版本库中的文件

##  关于远程仓库
-   git push origin master   推送到远程仓库
-   git clone -    git@github.com:PrettyMask/learngit.-    git  从远程仓库克隆

##  分支
-   git branch dev  创建名为 dev 的分支
-   git checkout dev  切换到dev分支
-   git merge dev 合并dev分支
-   git branch -d dev 删除分支dev
-   git branch 查看分支并确定当前分支






