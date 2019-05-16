def SelectSort(nums):
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)):
            m=nums[i]
            m_index=i
            if nums[j]<m:
                m=nums[j]
                m_index=j
        nums[i],nums[m_index]=nums[m_index],nums[i]
    return nums
