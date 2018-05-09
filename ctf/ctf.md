# CTF

##  1.  binwalk

- 2018.4.2----判断一个文件类型，并可以 自动提取 `binwalk -e [filename]`
- 2018.4.18---判断是否存在后门，原理未知



##  2.  Ziperello zip密码破解工具

##  3.  加密解密
-   回旋13踢
    -   ROT13（回转13位）是一种简易的替换式密码算法。
    -   解密 http://www.mxcz.net/tools/rot13.aspx

-   Bacon 加密法
    -   两个不同的符号，如 A 表示 0，B 表示 1。这个两个不同的符号，当然是可以其它的，如'+'和'-' 等，或者是不同的两种字体.  

    >​那么a到z对应的，密码表:  
    
        a AAAAA     g AABBA    n ABBAA    t BAABA
        b AAAAB    h AABBB   o ABBAB    u-v BAABB
        c AAABA    i-j ABAAA   p ABBBA    w BABAA
        d AAABB    k ABAAB    q ABBBB    x BABAB
        e AABAA    l ABABA    r BAAAA     y BABBA
        f AABAB    m ABABB    s BAAAB     z BABBB
    >  如果收到的密文是:
    AAAAB AAAAA ABAAA AAABB BAABB，则明文是 baidu， bajdu，baidv, bajdv， 我们就很容易知道它的正确意思是baidu.​

-   RSA
    -   第一步，随机选择两个不相等的质数p和q。
        -   爱丽丝选择了61和53。（实际应用中，这两个质数越大，就越难破解。）
    -   第二步，计算p和q的乘积n。
        -   爱丽丝就把61和53相乘。
        -   n = 61×53 = 3233
        -   n的长度就是密钥长度。3233写成二进制是110010100001，一共有12位，所以这个密钥就是12位。实际应用中，RSA密钥一般是1024位，重要场合则为2048位。
    -   第三步，计算n的欧拉函数φ(n)。
        -   根据公式：
            - φ(n) = (p-1)(q-1)
        -   爱丽丝算出φ(3233)等于60×52，即3120。
    -   第四步，随机选择一个整数e，条件是1< e < φ(n)，且e与φ(n) 互质。
        -   爱丽丝就在1到3120之间，随机选择了17。（实际应用中，常常选择65537。）
    -   第五步，计算e对于φ(n)的模反元素d。
        -   所谓"模反元素"就是指有一个整数d，可以使得ed被φ(n)除的余数为1。
            -   ed ≡ 1 (mod φ(n))
        -   这个式子等价于
            -   ed - 1 = kφ(n)
        -   于是，找到模反元素d，实质上就是对下面这个二元一次方程求解。
            -   ex + φ(n)y = 1
        -   已知 e=17, φ(n)=3120，
            -   17x + 3120y = 1
        -   这个方程可以用"扩展欧几里得算法"求解，此处省略具体过程。总之，爱丽丝算出一组整数解为 (x,y)=(2753,-15)，即 d=2753。
    -   第六步，将n和e封装成公钥，n和d封装成私钥。
        -   在爱丽丝的例子中，n=3233，e=17，d=2753，所以公钥就是 (3233,17)，私钥就是（3233, 2753）。
-   摩斯电码
-   凯撒
-   base32 64
    -   看到编码内容，只有大写和数字，根据Base64和Base32 区别：
        -   base64中包含大写字母（A-Z）、小写字母（a-z）、数字0——9以及+/；
        -   base32中只有大写字母（A-Z）和数字234567
## 4.   PHP
-   md5函数不能对数组进行处理
-   `strcmp()`函数可以不可以对数组处理
    ```php
        if (isset($_GET['a'])) {  
            if (strcmp($_GET['a'], $flag) == 0)  
                    die('Flag: '.$flag);  
             else  
                    print '离成功更近一步了';  
        }
        //提交： a[]=1
    ```

## 5.   Web
-   注意抓包
-   仔细观察
-   扫描发现了  .git    ???

-  #  注入：
     - 发现会网站会检查输入，过滤关键字，如：`index.php?id=1 order by 3 ` 会被过滤，可以考虑用如下的方式：
     - `index.php?id=1 or<>der by 3 `
     - `index.php?id=1 or/**/der by 3 `
     - **一个原则：语句正确才会执行**
     - 用join方式代替    `**,**`  如
        - `union select * from ((select user()) a join (select version())b)`==`union select user(),version()`
        - **起别名**
        - 将#进行URL编码 %23
    - ### sql注入绕过技巧
        - [sql注入绕过技巧](http://www.cnblogs.com/Vinson404/p/7253255.html)
        - 绕过空格
            - 两个空格代替一个空格，用Tab代替空格，%a0=空格：
            - `%20 %09 %0a %0b %0c %0d %a0 %00 /**/  /*!*/`
-  `user.php`
-  `user.php.bak`
-  可以用浏览器修改浏览器内的标签
-  index.php.txt

-   #   某次文件泄露题目
    -   扫描发现 .git文件泄漏
    -   通过githack.py下载泄漏的文件（linux）
    -   直接 git log 查看记录 然后 git diff <版本号>  <版本号> 对比信息
    -   然后发现 vim编辑器的恢复文件  .swo
    -   下载 .swo文件后 将名字改为 .swp
    -   对于  a.php.swp  重命名为   **.a.php.swp** 然后用 `vim -r a.php`即可查看源文件


-   #   UTF7编码
    -   在callback处有url编码，解码得：`+/v+ +ADwAcwBjAHIAaQBwAHQAPgBhAGwAZQByAHQAKAAiAGsAZQB5ADoALwAlAG4AcwBmAG8AYwB1AHMAWABTAFMAdABlAHMAdAAlAC8AIgApADwALwBzAGMAcgBpAHAAdAA+AC0-`

    -   由+/v+知是utf-7编码
-   #   HTTP头
    -   通过名字就知道，X-Forwarded-For 是一个 HTTP 扩展头部
    -   X-Forwarded-For 请求头格式非常简单，就这样：`X-Forwarded-For: client, proxy1, proxy2`
    -   如果一个 HTTP 请求到达服务器之前，经过了三个代理 Proxy1、Proxy2、Proxy3，IP 分别为 IP1、IP2、IP3，用户真实 IP 为 IP0，那么按照 XFF 标准，服务端最终会收到以下信息：  
    `X-Forwarded-For: IP0, IP1, IP2`       
    -   client-ip:127.0.0.1 也可以用来修改IP值

-   # MD5相关
    -   php中 0e******=0e*****
    -   hash拓展攻击