# 关于连接Ubuntu

## 首先需要打开22号端口

打开Ubuntu SSH 22端口的方法如下：需要安装OpenSSH server

使用命令安装：`sudo apt-get install openssh-server`
然后重启配置文件:`sudo /etc/init.d/ssh restart`

##  配置通过密钥连接ssh
-   首先在服务器上制作密钥对。首先用<font color="blue">**密码登录到你打算使用密钥登录的账户**</font>，然后执行以下命令：
` ssh-keygen`  
用户的home目录中生成了一个 .ssh 的隐藏目录，内含两个密钥文件。id_rsa 为私钥，id_rsa.pub 为公钥.
-   键入以下命令，在服务器上安装公钥：  

    `cd .ssh`  
    `cat id_rsa.pub >> authorized_keys`

-   如此便完成了公钥的安装。为了确保连接成功，请保证以下文件权限正确：

    `chmod 600 authorized_keys`  
    `chmod 700 ~/.ssh`   --这里路径需要更改

-   设置 SSH，打开密钥登录功能 

    -   编辑 /etc/ssh/sshd_config 文件，进行如下设置：  
        RSAAuthentication yes  
        PubkeyAuthentication yes
    -   另外，请留意 root 用户能否通过 SSH 登录：  
    `PermitRootLogin yes`
    -   当你完成全部设置，并以密钥方式登录成功后，再禁用密码登录：  
    `PasswordAuthentication no`  可选
    -   最后，重启 SSH 服务：

        `service sshd restart`