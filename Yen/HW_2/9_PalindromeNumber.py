class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # 如果(字串形式的 x == 反轉的自己)， 則 return true
        return str(x) == str(x)[::-1]

s9 = Solution()
a = s9.isPalindrome(-121)
print(a)