class Solution:
    def isPalindrome(self, x):
        x=str(x)
        return x==x[::1]
s1=Solution()
s="121"
print(s1.isPalindrome(s))
