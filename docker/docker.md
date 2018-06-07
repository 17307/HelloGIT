# docker
-   开启docker服务
-   
        # service 命令的用法
        $ sudo service docker start
        # systemctl 命令的用法
        $ sudo systemctl start docker
-   镜像
-   
        # 列出本机的所有 image 文件。
        $ docker image ls
        # 删除 image 文件
        $ docker image rm [imageName]

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
