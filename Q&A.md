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
