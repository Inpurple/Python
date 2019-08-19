常见问题答疑
====  
### 1.github和git的区别
git 是一个版本管理工具，是可以在你电脑不联网的情况下，只在本地使用的一个版本管理工具，其作用就是可以让你更好的管理你的程序，
比如你原来提交过的内容，以后虽然修改了，但是通过git这个工具，可以把你原来提交的内容重现出来，这样对于你后来才意识到的一些错误的更改，可以进行还原。

关于github，这是一个网站，就是每个程序员自己写的程序，可以在github上建立一个网上的仓库，你每次提交的时候可以把代码提交到网上，这样你的每次提交，别人也都可以看到你的代码，同时别人也可以帮你修改你的代码，这种开源的方式非常方便程序员之间的交流和学习。 

### 2.python list 和dict的查找效率比较
in 

```python
import time

query_lst = [-60000,-6000,-600,-60,-6,0,6,60,600,6000,60000]

lst = []
dic = {}

for i in range(100000000):
    lst.append(i)
    dic[i] = 1 

start = time.time()
for v in query_lst:
    if v in lst:
        continue
end1 = time.time()

for v in query_lst:
    if v in dic:
        continue

end2 = time.time()

print "list search time : %f"%(end1-start)
print "dict search time : %f"%(end2-end1)

```
运行结果：
list search time : 11.836798 
dict search time : 0.000007

python中list对象的存储结构采用的是线性表，因此其查询复杂度为O(n),而dict对象的存储结构采用的是散列表(hash表)，其在最优情况下查询复杂度为O(1)。

### 3.如何提高python运行效率

1.数据结构一定要选对，能用字典就不用列表
2.多用python封装好的库
3.循环之外能做的事不要放在循环内，比如下面的优化可以快一倍：

web项目的优化方法：
前端优化：
1.减少http请求
2.使用浏览器缓存
3.启用压缩
4.css放在页面最上部，javascript放在页面最下面。

服务器优化：
合理使用缓存
异步操作
使用集群
代码优化
存储优化

### 4.常见的linux命令？

cd，
pwd，显示当前a目录：pwd
touch，
ls，
mkdir，
rm，
help，
sudo，
ssh，
date，
clear

### 5.python中yield的用法？


### 6.cookie 是什么?

Cookie，有时也用其复数形式 Cookies，指某些网站为了辨别用户身份、进行 session 跟踪而储存在用户本地终端上的数据（通常经过加密）

cookie
存储的数据量小，最大不超过3k<br> 
是web服务器创建，在浏览器中存储<br> 
首次登录的时候服务器会创建cookie存储到浏览器中。<br> 
是浏览器的会话技术，是一种长连接的会话技术<br> 
它能够保证我们在有效期内，访问同一个web服务器时，产生比较好的体验。比如，自动登录操作。<br> 

session<br> 
session依赖于cookie<br> 
session属于服务器端的会话技术，一般会将数据保存在服务器端的内存或文件中<br> 
session可以保存较大的信息，但是由于它保存在服务器端，所以session数量不宜过多，如果过多，会占用服务器的内存过多，会影响服务器的性能<br> 
Django对session做了封装操作，session存储在数据库中<br> 

### 7.什么是CSS，什么是JS

层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。 [1] 
CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。

JavaScript一种直译式脚本语言，是一种动态类型、弱类型、基于原型的语言，内置支持类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在HTML（标准通用标记语言下的一个应用）网页上使用，用来给HTML网页增加动态功能


### 8.redis和Mysql的区别
1.redis 是非关系型数据库，数据存储在内存中，速度快。
2.Mysql 是关系型数据库，持久化存储，放在磁盘中，功能强大，检索是会用到一定的IO，数据访问也慢。
