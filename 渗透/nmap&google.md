# NMAP
-   Nmap常用命令参数讲解
-   -d [level] (提高或设置调试级别) 。 
-   -sT tcp端口扫描(完整三次握手)。
-   -sU udp扫描。(不回应可能端口打开,回应是关闭) 
-   -sL dns反向解析。    
-   -sM[fin ack mainmon扫描] 。
-   -sS隐蔽扫描(半开syn)。
-   -sP发现扫描网络存活主机。(直连arp非直连tcp80 icmp)
-   -sO确定主机协议扫描。
-   -sA tcp ACK扫描。
-   -sW 对滑动窗口的扫描sI[idlescan]。
-   -sR  RPC扫描。(flag没有syn,ack,rst回送rst)
-   -sN 关闭主机发现【空】。(不管是否存在直接扫描)
-   -sF FIN扫描 。(sN sF sX逃避不了ids)
-   -sX Xmas扫描 (fin psh urg为置位)。
-   -sI 完全隐藏。【以一个跳板主机{无流量}扫描另一台主机】
-   -sV 服务版本。
-   -sC 跟安全有关的脚本
-   -P0 指定协议。(不ping主机)(1icmp6tcp17udp47gre50esp51ah53swipe77sun-nd115l2tp120uti132sctp) 
-   -PS 端口列表用,隔开[tcp80 syn 扫描]
-   -PA 端口列表用,隔开[ack扫描](PS+PA测试状态包过滤防火墙【非状态的PA可以过】)【默认扫描端口1-1024】
-   -PU 端口列表用,隔开[udp高端口扫描 穿越只过滤tcp的防火墙]
-   -PE [icmp ping types]
-   -PM 掩码请求。
-   -PR [arp ping] 默认直连用。
-   -PN 自己。
-   -PP 时间请求。

#   Google

-   ps：不区分大小写
-   all开头一次查询只能使用一个
-   intext:关键词 （搜索页面正文包含关键词的网页）
-   allintext:关键词,关键词 （拼接多个关键词）
-   intitle:关键词 （搜索页面标题包含关键词的网页）
-   allintitle:关键词,关键词 （拼接多个关键词）
-   cache:url （搜索特定页面的快照）
-   defind:关键词 （搜索关于关键词的定义，不能与其他操作符混用）
-   filetype:关键词 （搜索所有以关键词为后缀的文件的url） 
-   ext:关键词 （性质与filetype一致）
-   info:  
    搜索输入URL的摘要信息和其他相关信息，该操作符不能与其他操作符及关键字混用
-   inurl:关键词 （搜索url中包含关键词的网页）
-   allinurl:关键词,关键词 （搜索url中包含多个关键词的网页）
-   site:url （将搜索范围缩小到特定的网站，域或子域）
-   *（通配符）
-   -（排除符号）