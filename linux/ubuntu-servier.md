#   记一次ubuntu-server安装

-   ## 从官网下载好镜像，制作U盘启动器。
    -   选择工具为：`UltraISO`，但安装过程中会出现：无法从CD-ROM中找到镜像的问题……以及后面一系列问题。
    -   解决方法：将`Ubuntu`镜像`copy`到U盘中，然后手动挂载，或者扫描U盘。
    -   后经一位师兄提醒，将制作工具换为：`Win32DiskImager`.然后一切正常。

-   ## raid卡配置
    -   服务器有两块硬盘，需要配置raid卡。
    -   本服务器通过`CTRL+M`进入配置页面。将两个硬盘的`raid`全都设置为`0`，然后重新初始化。
    -   `raid0`与`raid1`区别：
        -   如果2块硬盘，均为10GB.
        -   `raid0`模式中，最后的硬盘容量是 `10GB+10GB=20GB`
        -   `raid1`模式中，最后的硬盘容量是 `10GB+10GB=10GB`，其中一块硬盘是另一块硬盘的备份。
-   ## 进入 `bios` 页面，然后再`boot`选项中选择配置U盘 启动优先，或者直接选择U盘启动。


-   ## 在配置过程中，遇到的最大的<font color="blue">**坑**</font>。
    -   出现了`unable to install grub in /dev/md126X`


            关键点是在安装ubuntu的时候，安装grub所产生了错误，导致系统无法启动。
            其实ubuntu 12.04已经支持了这块服务器的megaraid软RAID的驱动，在内核目录能看到驱动程序（也可以从官网上下载）。
            所以在做分区的时候，其实也是能搜索到这个磁盘的，只是dev的名字有点怪，叫/dev/md126
            关键点是需要手工echo "(hd0) /dev/md126" > /boot/device.map,然后grub-install 到/dev/md126上。
            因为在raid的安装上，如果要mount到合适的/boot分区，就必须mount到/dev/md126pX这种设备上，而这些设备是没有所谓MBR的，而GRUB的安装参数则必须要放到/dev/md126上，这个小小的差异就导致了问题。
    -   解决方案
        -   当遇到了`unable to install grub in /dev/md126X`时，首先深呼吸，接杯水压压惊。
        -   Now we start to install GRUB by our hand:
        -   `ALT+F2`进入cmd界面
        -   首先`ls -al`看看有没有`target`这个文件夹，
            -   如果有就进到`target`中，
                -   看看有没有`home`这个文件夹，如果还是有……就`mount /dev/md126pX /target/home`
                -   如果没有`home`就`mount /dev/md126pX /target`
            -   如果没有就`mkdir target`,然后 `mount /dev/md126pX /target`
            -   "X" is your partion dev number, you should know it from prev installation process.
        -  `# mount -o bind /proc /target/proc`

        -  `# mount -o bind /sys /target/sys`

        -  `# mount --rbind /dev /target/dev`
        -  （Now we do a chroot to the mount system.）  
        `# chroot /target /bin/bash`
        -   (Now create the file device.map, used by GRUB.）  <br><br>
        `# echo "(hd0) /dev/md126" > /boot/device.map`  <br><br>
        <font color="red">**NOTE THAT**:</font><font color="blue"> use /dev/md126, NOT /dev/md126p1, it should the "md126"!</font>
        -   `# cp /boot/device.map /boot/grub/`
        -   Now install grub  
            `# grub-install --root-directory=/ /dev/md126 `  
            `# grub-setup /dev/md126`  
            没有此工具，不执行也没什么问题
        -   `# update-grub`  
            It will build the file: /boot/grub/grub.cfg  
            Done.

    -
            The key process is # echo "(hd0) /dev/md126" > /boot/device.map
            Becaulse the Ubuntu installation program use the /target partition /dev/md126p1 directory in grub-install, so it can't be done in a raid. The RAID MBR is not on the first partition /dev/md126p1,  but on the base devices file /dev/md126
        -  看到done后，`ALT+F1`退出命令行，重新安装gurb即可。