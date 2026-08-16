class Solution(object):
    def removeElement(self, nums, val):
     v=0
     for i in range(len(nums)):
         if nums[i]!=val:
            nums[v]=nums[i]
            v+=1
     return v
s1=Solution()
nums=[3,2,2,3]
val=2
print(s1.removeElement(nums,val))
