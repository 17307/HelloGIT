# docker
-   ## 开启docker服务
-   
        # service 命令的用法
        $ sudo service docker start
        # systemctl 命令的用法
        $ sudo systemctl start docker

-   # 基本操纵
-   ##  image与container
    从仓库中将img文件下载下来  
    `$ docker image pull library/hello-world  `  
    > docker image pull是抓取 image 文件的命令。library/hello-world是 image 文> 件在仓库里面的位置，其中library是 image 文件所在的组，hello-world是 image > 文件的名字
    > 由于 Docker 官方提供的 image 文件，都放在library组里面，所以它的是默认组，> 可以省略。因此，上面的命令可以写成下面这样。
    `$ docker image pull hello-world`

    列出本机的所有 image 文件。  
    `$ docker image ls  `  
    删除 image 文件  
    `$ docker image rm [imageName] ` 

    现在，运行这个 image 文件。

    `$ docker container run hello-world`  
    `docker container run` 命令会从 image 文件，生成一个正在运行的容器实例。  
    `docker container run` 命令具有自动抓取 image 文件的功能。如果发现本地没有指定的 image 文件，就会从仓库自动抓取。因此，前面的`docker image pull`命令并不是必需的步骤。

    `$ docker container run -it ubuntu bash` 运行ubuntu并且体验bash  
    `$ docker container kill [containID]` 杀死某个docker容器  
    `$ docker container rm [containerID]` 删除某个容器文件

-   ## Dockerfile
-   构建镜像  
    `FROM nginx`   
    `RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html`
    -  ### FROM 指定基础镜像  <br>Dockerfile 中 FROM 是必备的指令，并且必须是第一条指令
    -  RUN 指令是用来执行命令行命令的。由于命令行的强大能力，RUN 指令在定制镜像时是最常用的指令之一。其格式有两种:<br>
        -  shell 格式：RUN <命令>，就像直接在命令行中输入的命令一样。刚才写的 Dockerfile 中的 RUN 指令就是这种格式。
        -  exec 格式：RUN ["可执行文件", "参数1", "参数2"]，这更像是函数调用中的格式
        - <font color="red">注意，每一次run都会构建一次新的镜像，所以最好把多个命令写一起。</font>
-   build镜像
    -   docker build [选项] <上下文路径/URL/->
    -   在 Dockerfile 文件所在目录执行：`docker build -t nginx:v3 .`
    -   注意后面的 `.`
    -   

#   搭建wordpress

-   ##  首先，新建一个工作目录，并进入该目录
    -   `$ mkdir docker-demo && cd docker-demo`
-   ##  在docker-demo目录下，新建docker-compose.yml文件，写入下面的内容。
    -
            mysql:
                image: mysql:5.7
                environment:
                - MYSQL_ROOT_PASSWORD=123456
                - MYSQL_DATABASE=wordpress
            web:
                image: wordpress
                links:
                - mysql
                environment:
                - WORDPRESS_DB_PASSWORD=123456
                ports:
                - "0.0.0.0:8080:80"
                working_dir: /var/www/html
                volumes:
                - wordpress:/var/www/html

-   ##  上面代码中，两个顶层标签表示有两个容器mysql和web。每个容器的具体设置，前面都已经讲解过了，还是挺容易理解的。
-   ##  启动两个容器。
    -   `docker-compose up`
-   ##  关闭
    -   `docker-compose stop`
-   ## 关闭以后，这两个容器文件还是存在的，写在里面的数据不会丢失。下次启动的时候，还可以复用。
-   ## 下面的命令可以把这两个容器文件删除（容器必须已经停止运行）。  
    -   `$ docker-compose rm`
