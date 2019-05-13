1.	Python continue 语句
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。

2.	带索引的列表迭代 enumerate()  
列表：
 
字典：对键和值都进行遍历
如果只需要值，可以使用d.values，如果想获取所有的键则可以使用d.keys。
如果想获取键和值d.items方法会将键-值对作为元组返回，for循环的一大好处就是可以循环中使用序列解包。
代码实例：
1
2
3
4
5	for key, value in d.items():
    print (key, ' value : ', value)
name1 value : pythontab
name2 value : .
name3 value : com

3.	Python标准库网址
https://docs.python.org/zh-cn/3/library/index.html

4.	Python中的浅拷贝和深拷贝
Python的切片操作是是浅拷贝
浅拷贝
>>> import copy
>>> a = [1, 2, 3, [5, 6]]
>>> b = copy.copy(a)
>>> print b
[1, 2, 3, [5, 6]]
>>> a[3].append('c')
>>> print b
[1, 2, 3, [5, 6, 'c']]
深拷贝
>>> a = [1, 2, 3, [5, 6]]
>>> b = copy.deepcopy(a)
>>> a[3].append('c')
>>> print b
[1, 2, 3, [5, 6]]
拷贝即是开辟一块新的内存空间，把被拷贝对象中的值复制过去。而浅拷贝并没有为子对象[5,6]开辟一块新的内存空间，而仅仅是实现对a中[5，6]的引用。所以改变a中[5，6]的值，b中的值也会发生变化。
深拷贝则是为子对象也开辟了一块新空间。所以改变a中[5, 6]的值，并不影响b

5.	python根据某个值获得一维列表和二维列表的索引值
#一维列表  
L1 = [1,2,3,4,5,6,7,8,9,10]  
#二维列表  
L2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]  

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


s.index(x[, i[, j]])	x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前）

6.	不同于我用过的其它编程语言，Python 没有 switch / case 语句。为了实现它，我们可以使用字典映射：

7.	Python中可以当做key值的数据类型：
所以所有python自带类型中，除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key

8.	可变类型和不可变类型
不可变对象：该对象所指定内存中的值不可以被改变，在改变某个对象的值的时候，由于其内存中的值不可以被改变，所以，会把原来的值复制一份再进行改变，这样就会计算机会开辟一段新的内存空间来存储新的值，python 不可变对象有 int str float number,tuple,None
可变对象：该对象所指定的内存地址上面的值可以被改变，变量被改变后，其所指向的内存地址上面的值，直接被改变，没有发生复制行为，也没有发生开辟新的内存地址行为。python可变对象有，列表，字典，set集合

9.	Python中在列表索引超出范围(这里：’’)时获得默认值。
我如何做到这一点？在Python的“请求宽恕，不允许”的精神，这里有一种方法：
try:
    b = a[4]
except IndexError:
    b = ''
    
10.	python中关于str与list的替换
字符串替换str.replace()方法
python中的replace()方法是把字符串中的old字符串替换成new的字符串，如果指定替换次数max,则按照替换次数进行替换
str.replace(old,new,count=0)
old：字符串替换前的字符 
new：字符串替换后的字符 
count：替换的次数，默认为0，不填表示全局替换
列表替换直接用索引赋值法

11.	字典序的理解
设想一本英语字典里的单词，何者在前何者在后？
显然的做法是先按照第一个字母、以 a、b、c……z 的顺序排列；如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。如果比到最后两个单词不一样长（比如，sigh 和 sight），那么把短者排在前。
通过这种方法，我们可以给本来不相关的单词强行规定出一个顺序。“单词”可以看作是“字母”的字符串，而把这一点推而广之就可以认为是给对应位置元素所属集合分别相同的各个有序多元组规定顺序。

12.	python 字符相减得到数字
python中没有字符之间的直接相减运算，但可以通过ord()函数实现 
ord()函数主要用来返回对应字符的ascii码
>>> ord('9')-ord('0')
9

13.	如何删除二维数组的列
import numpy as np
A = np.delete(A, 1, 0)  # delete second row of A
B = np.delete(B, 2, 0)  # delete third row of B
C = np.delete(C, 1, 1)  # delete second column of C
According to numpy's documentation page, the parameters for numpy.delete are as follow:
numpy.delete(arr, obj, axis=None)
•	arr refers to the input array,
•	obj refers to which sub-arrays (e.g. column/row no. or slice of the array) and
•	axis refers to either column wise (axis = 1) or row-wise (axis = 0) delete operation.

14.	SET的用法
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.
Python Set add()方法
add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
语法
add()方法语法：set.add(elmnt)

15.	超出索引的返回值
pattern="b"
print(pattern[1:])—None
print(pattern[1])---提示超出索引

16.python list中方法的时间复杂度
Operation	Big-O Efficiency
index []	O(1)
index assignment	O(1)
append	O(1)
pop()	O(1)
pop(i)	O(n)
insert(i,item)	O(n)
del operator	O(n)
iteration	O(n)
contains (in)	O(n)
get slice [x:y]	O(k)
del slice	O(n)
set slice	O(n+k)
reverse	O(n)
concatenate	O(k)
sort	O(n log n)
multiply	O(nk)

17. python ‘//’ 取整，‘%’ 取余
>>> 2/2   除法
1.0
>>> 2//2  取整
1
>>> 1/2   除法
0.5
>>> 1//2  取整
0
>>> 3//2  取整
1
>>> 3%2  取余
1
>>> 4%2  取余
0

18.list与str的呼唤
对python 字符串中指定位置的字符做修改操作：
str = list(str)
str [0] = 'p'
str = '.join(str)

19. Python 字符串大小写转换
以下代码演示了如何将字符串转换为大写字母，或者将字符串转为小写字母等：
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

20.Python中可以用如下方式表示正负无穷：
float("inf"), float("-inf")

