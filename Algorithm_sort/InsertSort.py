
def InsertSort(nums):
"""
简单插入排序(Insert Sort)
从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素（称为target元素），在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，交换相邻的元素；
直到target大于正在遍历的已排序元素
重复步骤

每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。

额外空间开销出在数据移位时那一个过渡空间，空间复杂度O(1)。

"""
    for i in range(1,len(nums)):#从角标为1，到最后一位，注意角标。
        j=i-1
        target=nums[i]
        while j>=0 and target<nums[j]:#不满足则退出循环
            nums[j],nums[j+1]=nums[j+1],nums[j]#满足调节相邻交换
            j=j-1
        print(nums)
    return(nums)
