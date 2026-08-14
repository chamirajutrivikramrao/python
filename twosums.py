class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return(i,j)
s1=Solution()
target=9
nums=[1,4,5,2]
print(s1.twoSum(nums,target))
        
