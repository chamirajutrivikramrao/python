class Solution:
    def removeDuplicates(self, nums):
        v=[]
        for i in nums:
            if i not in nums:
                v.append(i)
        return v
s1=Solution()
nums=[1,2,3,1,4]
print(s1.removeDuplicates(nums))
