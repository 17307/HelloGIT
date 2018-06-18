#   Docker && mongodb

- ## 构建环境
    - `docker pull mongo:3.2`
    - `docker run -p 27017:27017 -v $PWD/db:/data/db -d mongo:3.2`
    
        >`-p 27017:27017` : 将容器的27017 端口映射到主机的27017 端口  
        >`-v $PWD/db:/data/db` : 将主机中当前目录下的db挂载到容器的/data/db，作为mongo数据存储目录
    - `docker run -it mongo:3.2 mongo --host 172.17.0.1`
        > `docker run -it mongo:3.2` 运行这个镜像 然后执行命令 `mongo --host 172.17.0.1 `
- ## mongodb

    - ### mongodb与sql型数据库类比
    
        | SQL术语/概念 | MongoDB术语/概念 | 解释/说明 |
        | ------------ | ---------------- | ------------------ |
        | database     | database         | 数据库                                          |
        | table        | collection       | 数据库表/集合                                   |
        | row          | document         | 数据记录行/文档                                 |
        | column       | field            | 数据字段/域                                     |
        | index        | index            | 索引                                            |
        | table        | joins            | 表连接,MongoDB不支持                            |
        | primary      | key              | primary key	主键,MongoDB自动将_id字段设置为主键 |

    - ### 数据库
        - 一个mongodb中可以建立多个数据库。   
            MongoDB的默认数据库为"db"，该数据库存储在data目录中。
        - `show dbs`
        - 执行 `db` 命令可以显示当前数据库对象或集合
        - 运行 `use` 命令，可以连接到一个指定的数据库  
            ` use local`

    - ### 文档
        - 文档是一组键值(key-value)对(即BSON)
            - 文档中的键/值对是有序的。
            - 文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
            - MongoDB区分类型和大小写。
            - MongoDB的文档不能有重复的键。
            - 文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。
    - ### 集合
        - 集合就是 MongoDB 文档组,类似与sql数据库中的表格
        - 可以将以下不同数据结构的文档插入到集合中:
            >{"site":"www.baidu.com"}  
            >{"site":"www.google.com","name":"Google"}  
            >{"site":"www.runoob.com","name":"菜鸟教程","num":5}  
    - ### 元数据
        - 数据库一些信息
    - ### MongoDB 数据类型
    - ### 数据库连接 
        - http://www.runoob.com/mongodb/mongodb-connections.html
    - ### 数据库操作
        - 创建数据库 `use DATABASE_NAME`
        - 切换到数据库 `use my_dababase` ; 然后删除数据库 `db.dropDatabase()`
        - ` show collections `显示集合
        - 创建集合
            - 1.通过`db.createCollection(name, options)`
            - 2.在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。
        - 删除集合
            > `use runoob `   
            switched to db runoob  
            > `show tables  `  
            site    
            > `db.site.drop() `   
            true  
            >` show tables`  
        - 创建文档
            - `db.COLLECTION_NAME.insert(document)`
            - `document = ({1:1})`  
              `db.col.insert(document)`
        - 更新文档
            - 方法一
                ```javascript
                db.collection.update(
                    <query>, # update的查询条件，类似sql update查询内where后面的。
                    <update>, # update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
                        {
                            upsert: <boolean>, # 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
                            multi: <boolean>, # 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
                            writeConcern: <document> # 可选，抛出异常的级别。
                        }
                    )
                ```
            >`db.col.update({'title':'MongoDB 教程'},{$set:{'title':'MongoDB'}})`
            -   方法二
           
            ```javascript
                /*save() 方法通过传入的文档来替换已有文档*/
                db.collection.save(
                <document>,
                {
                    writeConcern: <document>
                }
                )
            ```
            - `db.collection.updateOne() 向指定集合更新单个文档`  
            - `db.collection.updateMany() 向指定集合更新多个文档`
        - 删除文档

            ```javascript
            deleteOne() 
            deleteMany()
            ```
            >如删除集合下全部文档：  
            >db.inventory.deleteMany({})  
            >删除 status 等于 A 的全部文档：  
            >`db.inventory.deleteMany({ status : "A" })`  
            >删除 status 等于 D 的一个文档：  
            >`db.inventory.deleteOne( { status: "D" } )`
        - 查询
            - `db.collection.find(query, projection)`
            >query ：可选，使用查询操作符指定查询条件  
            >projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。
            - AND
                - `db.col.find({"by":"菜鸟教程", "title":"MongoDB 教程"}).pretty()`
            - OR
                - `db.col.find({$or:[{"by":"菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()`
            - AND 和 OR
                - `db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()`
            -  projection 参数的使用方法
                -  `db.collection.find(query, {title: 1, by: 1}) // inclusion模式 指定返回的键，不返回其他键`
                -  `db.collection.find(query, {title: 0, by: 0}) // exclusion模式 指定不返回的键,返回其他键`
                -  两种模式不可混用（因为这样的话无法推断其他键是否应返回）
        -   条件查询
            -   `db.col.find({likes : {$lt : 150}})`
                >$gt -------- greater than  >  
                $gte --------- gt equal  >=  
                $lt -------- less than  <  
                $lte --------- lt equal  <=  
                $ne ----------- not equal  !=  
                $eq  --------  equal  =  
        -   `db.col.find({},{"title":1,_id:0}).limit(1).skip(1)`
        -   `db.COLLECTION_NAME.find().sort({KEY:1})`  1 为升序排列，而-1是用于降序排列
        -   `db.col.createIndex({"title":1,"description":-1})` 创建索引
        -   # 聚合