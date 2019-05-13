"""
1.2 快速排序(Quick Sort)
从数列中挑出一个元素，称为 “基准”（pivot）；
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
快速排序基于选择划分，是简单选择排序的优化。

每次划分将数据选到基准值两边，循环对两边的数据进行划分，类似于二分法。

算法的整体性能取决于划分的平均程度，即基准值的选择，此处衍生出快速排序的许多优化方案，甚至可以划分为多块。

基准值若能把数据分为平均的两块，划分次数O(logn)，每次划分遍历比较一遍O(n)，时间复杂度O(nlogn)。

额外空间开销出在暂存基准值，O(logn)次划分需要O(logn)个，空间复杂度O(logn)
"""



def partition(left,right,Array):
    
    key=left    
    while left<right:
        
        if Array[left]>Array[key] and Array[right]<Array[key]:
            Array[left],Array[right]=Array[right],Array[left]
            left+=1
            right-=1

        elif Array[right]>=Array[key]:#先判断right，目的是先停在小于等于Array[key]的指针上
            right-=1
        elif Array[left]<=Array[key]:
            left+=1
    #此时left&right相等
    Array[right],Array[key]=Array[key],Array[right]#替换的值一定要小于等于Array[key]
    print(Array[right],Array)
    return left#返回基值位置所在


def quicksort(left,right,array):#分治法
    if left>=right:
        return
    mid=partition(left,right,array)
    quicksort(left,mid-1,array)
    quicksort(mid+1,right,array)
    
array=[5,4,3,1,0,5,9,7]
left=0
right=len(array)-1
quicksort(left,right,array)
print(array)
