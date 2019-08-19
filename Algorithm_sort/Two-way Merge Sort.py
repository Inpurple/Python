"""
4. 归并排序
4.1 二路归并排序(Two-way Merge Sort)
归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。


"""
def merge(left,right,mid,nums):
    i=left
    j=mid+1
    temp=[]
    while i<=mid and j<=right:
        if nums[i]<nums[j]:
            temp.append(nums[i])
            i=i+1
        else:
            temp.append(nums[j])
            j=j+1
    while i<=mid:
            temp.append(nums[i])
            i=i+1
    while j<=right:
            temp.append(nums[j])
            j=j+1
    
    for k in range(len(temp)):
        nums[left+k]=temp[k]
        
    
def recur(left,right,nums):#假设为两个有序的再合并为一个有序的
    if left>=right:
        return
    mid=(left+right)//2
    recur(left,mid,nums)
    recur(mid+1,right,nums)
    merge(left,right,mid,nums)
    
array=[0, 0, 1, 3, 8, 0,100,-9,-30]
recur(0,len(array)-1,array)
print(array)
