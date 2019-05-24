Python 语法总结 
====

### 1.Python continue 语句
continue 语句跳出本次循环，而break跳出整个循环。 
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue 语句用在while和for循环中。

### 2.	带索引的列表迭代 enumerate() 
列表：<br>  
```python
teams=["Parkers","49ers","Ravens","Patriots"]
for index,team in enumerate(teams):
    print(index,team)
```
    0 Parkers
    1 49ers
    2 Ravens
    3 Patriots
 
字典：对键和值都进行遍历<br>  
如果只需要值，可以使用d.values()，如果想获取所有的键则可以使用d.keys()。
如果想获取键和值d.items方法会将键-值对作为元组返回，for循环的一大好处就是可以循环中使用序列解包。

```python
d={
name1: "pythontab",
name2: ".",
name3: "com"
}
for key, value in d.items():
    print (key, ' value : ', value)
```
    name1 value : pythontab<br>  
    name2 value : .<br> 
    name3 value : com<br> 

### 3.	Python标准库网址
https://docs.python.org/zh-cn/3/library/index.html

### 4.	Python中的浅拷贝和深拷贝<br> 
Python的切片操作是是浅拷贝<br> 
#### 浅拷贝
```python
import copy
a = [1, 2, 3, [5, 6]]
b = copy.copy(a)
print b
```
    [1, 2, 3, [5, 6]]
```python
a[3].append('c')
print b
```
    [1, 2, 3, [5, 6, 'c']]
#### 深拷贝
```python
a = [1, 2, 3, [5, 6]]
b = copy.deepcopy(a)
a[3].append('c')
print b
```
    [1, 2, 3, [5, 6]]
拷贝即是开辟一块新的内存空间，把被拷贝对象中的值复制过去。而浅拷贝并没有为子对象[5,6]开辟一块新的内存空间，而仅仅是实现对a中[5，6]的引用。所以改变a中[5，6]的值，b中的值也会发生变化。深拷贝则是为子对象也开辟了一块新空间。所以改变a中[5, 6]的值，并不影响b

### 5.	python根据某个值获得一维列表和二维列表的索引值

```python
L1 = [1,2,3,4,5,6,7,8,9,10]  #一维列表  

L2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]  #二维列表  

def getOneDimensionListIndex(L,value):  
"""获得一维列表某个值的索引值"""  
index = L.index(value)  
return index  


def getTwoDimensionListIndex(L,value):  
"""获得二维列表某个值的一维索引值 
思想：先选出包含value值的一维列表，然后判断此一维列表在二维列表中的索引 
"""  
data = [data for data in L if data[0]==value] #data=[(53, 1016.1)]  
index = L.index(data[0])  
return index

#获得二维列表某个值的一维索引值的另一种方法
def getTwoDimensionListIndex(L,value):  
    """获得二维列表某个值的一维索引值的另一种方法"""  
    for i in range(len(L)):  
        for j in range(len(L[i])):  
            if L[i][j] == value  
            index = i 
```
s.index(x[, i[, j]])	x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前）

### 6.Python 没有 switch / case 语句
不同于我用过的其它编程语言，Python 没有 switch / case 语句。为了实现它，我们可以使用字典映射：

### 7.	Python中可以当做key值的数据类型：
所有python自带类型中，除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key

### 8.	可变类型和不可变类型
不可变对象：该对象所指定内存中的值不可以被改变，在改变某个对象的值的时候，由于其内存中的值不可以被改变，所以，会把原来的值复制一份再进行改变，这样就会计算机会开辟一段新的内存空间来存储新的值，python 不可变对象有 int str float number,tuple,None<br>  

可变对象：该对象所指定的内存地址上面的值可以被改变，变量被改变后，其所指向的内存地址上面的值，直接被改变，没有发生复制行为，也没有发生开辟新的内存地址行为。python可变对象有，列表，字典，set集合

### 9.	Python中在列表索引超出范围(这里：’’)时获得默认值。
我如何做到这一点？在Python的“请求宽恕，不允许”的精神，这里有一种方法：<br> 
try:
    b = a[4]
except IndexError:
    b = ''
    
### 10.	python中关于str与list的元素替换

字符串替换str.replace()方法
python中的replace()方法是把字符串中的old字符串替换成new的字符串，如果指定替换次数max,则按照替换次数进行替换<br> 
str.replace(old,new,count=0)<br> 
old：字符串替换前的字符 <br> 
new：字符串替换后的字符 <br> 
count：替换的次数，默认为0，不填表示全局替换<br> 

列表替换直接用索引赋值法

### 11.	字典序的理解
设想一本英语字典里的单词，何者在前何者在后？<br> 
显然的做法是先按照第一个字母、以 a、b、c……z 的顺序排列；如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。如果比到最后两个单词不一样长（比如，sigh 和 sight），那么把短者排在前。<br>
通过这种方法，我们可以给本来不相关的单词强行规定出一个顺序。“单词”可以看作是“字母”的字符串，而把这一点推而广之就可以认为是给对应位置元素所属集合分别相同的各个有序多元组规定顺序。
### 12.	python 字符相减得到数字
python中没有字符之间的直接相减运算，但可以通过ord()函数实现 
ord()函数主要用来返回对应字符的ascii码
```python
ord('9')-ord('0')
```
    9
### 13.	如何删除二维数组的列
```python
import numpy as np
A = np.delete(A, 1, 0)  # delete second row of A
B = np.delete(B, 2, 0)  # delete third row of B
C = np.delete(C, 1, 1)  # delete second column of C
```
According to numpy's documentation page, the parameters for numpy.delete are as follow:
numpy.delete(arr, obj, axis=None)
* arr refers to the input array,
* obj refers to which sub-arrays (e.g. column/row no. or slice of the array) and
* axis refers to either column wise (axis = 1) or row-wise (axis = 0) delete operation.

### 14.	SET的用法
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.

#### set的创建：
集合(set)
a.set是一个无序不重复的序列

b.可以用 { } 或者 set( ) 函数创建集合

c.集合存放不可变类型（字符串、数字、元组）

　　注意：创建一个空集合必须用 set( ) 而不是 { } ，因为 { } 是用来创建一个空字典 

 
#### Python Set add()方法
add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
语法
add()方法语法：set.add(elmnt)

### 15.	超出索引的返回值
pattern="b"<br>
print(pattern[1:])—""<br>
print(pattern[1])---提示超出索引<br>

pattern=["b"]<br>
print(pattern[1:])—[]<br>
print(pattern[1])---提示超出索引
### 16.python list中方法的时间复杂度
#### list
|Operation|Big-O Efficiency|
|:---|:---|
|index [] | O(1)|
|index assignment | O(1)|
|append | O(1)|
pop() | O(1)
pop(i) | O(n)
insert(i,item) | O(n)
del operator | O(n)
iteration | O(n)
contains (in) | O(n)
get slice [x:y] | O(k)
del slice | O(n)
set slice | O(n+k)
reverse | O(n)
concatenate | O(k)
sort | O(n log n)
multiply | O(nk)

#### dic

|操作|平均情况|最坏情况|
|:---|:---|:---|
|复制|O(n)|O(n)|
|取元素|O(1)|O(n)|
|更改元素|O(1)|O(n)|
|删除元素|O(1)|O(n)|
|遍历|O(n)|O(n)|

#### set
|操作|平均情况|最坏情况|
|:---|:---|:---|
x in s|O(1)|O(n)
并集|s|t|O(len(s)+len(t))	 
交集|s&t|O(min(len(s), len(t))|O(len(s) * len(t))
差集|s-t|O(len(s))	 
s.difference_update(t)|O(len(t))	 
对称差集 s^t|O(len(s))|O(len(s) * len(t))
s.symmetric_difference_update(t)|O(len(t))|O(len(t) * len(s))

### 17. python ‘//’ 取整，‘%’ 取余
2/2   除法<br>  
1.0<br>  
2//2  取整<br>  
1<br>  
1/2   除法<br>  
0.5<br>  
1//2  取整<br>  
0<br>  
3//2  取整<br>  
1<br>  
3%2  取余<br>  
1<br>  
4%2  取余<br>  
0<br>  

### 18.list与str的转换
对python 字符串中指定位置的字符做修改操作：<br>  
```python
str = list(str)
str [0] = 'p'
str = '.join(str)
```
### 19. Python 字符串大小写转换
以下代码演示了如何将字符串转换为大写字母，或者将字符串转为小写字母等：
```Python
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 
```

### 20.Python中可以用如下方式表示正负无穷：

float("inf")<br>  
float("-inf")

### 21.Python split()方法
Python 字符串 Python 字符串

#### 描述
Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

#### 语法
split() 方法语法：
```python
str.split(str="", num=string.count(str)).
```
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。<br> 
num -- 分割次数。默认为 -1, 即分隔所有。<br> 
返回值:返回分割后的字符串列表。

### 22.解决报错RecursionError: maximum recursion depth exceeded in comparison
发现python默认的递归深度是很有限的（默认是1000），因此当递归深度超过999的样子，就会引发这样的一个异常。
解决<br> 
可以修改递归深度的值，让它变大大一点
```python
import sys   
sys.setrecursionlimit(100000) #例如这里设置为十万  
```
结语<br> 
这个解决方法并不治本，还需要在代码上进行优化。我出现这个错误的原因是忽略了对爬取页面的异常值处理，在增加判断之后，递归深度一般达不到python的默认限制。

### 23.Python 排序---sort与sorted学习
当我们从数据库中获取一写数据后，一般对于列表的排序是经常会遇到的问题，今天总结一下python对于列表list排序的常用方法：
#### 第一种：内建方法list.sort()可以直接对列表进行排序
用法：
```python
list.sort(func=None, key=None, reverse=False(or True))
```
对于reverse这个bool类型参数，当reverse=False时：为正向排序；当reverse=True时：为方向排序。默认为False。
执行完后会改变原来的list，如果你不需要原来的list，这种效率稍微高点为了避免混乱，其会返回none
例如：
```python
list = [2,8,4,6,9,1,3]
list.sort()
print(list)
```
    [1, 2, 3, 4, 6, 8, 9]+
#### 第二种：内建函数sorted()<br>
这个和第一种的差别之处在于：
sorted()不会改变原来的list，而是会返回一个新的已经排序好的list<br>
list.sort()方法仅仅被list所定义，sorted()可用于任何一个可迭代对象<br>
用法：
```python
sorted(list)
```

该函数也含有reverse这个bool类型的参数，当reverse=False时：为正向排序(从小到大)；当reverse=True时：为反向排序(从大到小)。当然默认为False。
执行完后会有返回一个新排序好的list
例如：

>>> list = [2,8,4,1,5,7,3]
>>> other = sorted(list)
>>> other
[1, 2, 3, 4, 5, 7, 8]

### 24.反转部分列表
#### 方法1：切片法
```python
a = [1,2,3,4,5]
a[0:3] = a[2::-1]   #work! 参数略复杂，[]中第一个参数是要反转的最后一个数的index，比如这里要翻转前三个数字 1 2 3，
               #那么第一个参数就是3的index，所以这里是2，第二个参数是要反转的第一个数的index，如果从第一个数开始那么可以省略
               #最后一个参数是-1，表示反序
print(a)
>>[3, 2, 1, 4, 5]
```
#### 方法2：list.reverse()
list.reverse()：是python中列表的一个内置方法（也就是说，在字典，字符串或者元组中，是没有这个内置方法的），用于列表中数据的反转；
exp：
```python
lista = [1, 2, 3, 4]
lista.reverse()
print(lista)
```
1
2
3
    打印结果：[4, 3, 2, 1]

其实，lista.reverse() 这一步操作的返回值是一个None，其作用的结果，需要通过打印被作用的列表才可以查看出具体的效果。

#### 方法3：reversed()：
而reversed()是python自带的一个方法，准确说，应该是一个类；<br>
关于reversed()官方解释：

>reversed(sequence) -> reverse iterator over values of the sequence
>Return a reverse iterator

translate it :
>reversed（sequence） - >反转迭代器的序列值
>返回反向迭代器

也就是说，在经过reversed()的作用之后，返回的是一个把序列值经过反转之后的迭代器，所以，需要通过遍历，或者List,或者next()等方法，获取作用后的值；

下面通过几个案例进行说明：
1.列表的反转：
```python
bb = [1,3,5,7]
print(list(reversed(bb)))
```
1
2
    打印结果：[7, 5, 3, 1]

### 25.dic.get()方法
get() 方法语法：

D.get(key[,default=None])
参数<br>
key -- 字典中要查找的键。<br>
default -- 可选参数，如果指定键的值不存在时，返回该值，默认为 None。<br>
返回值<br>
返回指定键的值，如果指定键的值不在字典中返回指定值，默认为 None。

### 26.python 中 None，空字符串，空列表的区别：
#### 1.区别:数据类型
在python中是没有NULL的，取而代之的是None，它的含义是为空，但要注意和空列表与空字符串的区别，None的类型是Nonetype,""的类型是string，[]的类型是list.

#### 2.共同点：判断皆为False
```python
type(None)
>>><class 'NoneType'>
```
python是把0，空字符串‘ ’和None都看作False，把其他数值和非空字符串都看作True

