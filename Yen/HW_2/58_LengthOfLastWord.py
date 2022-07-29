class Solution:
    def lengthOfLastWord(self, s: str) -> int:\
        
        # 刪除最後面的空格、用空格分開字串，變成 list 形式
        s = s.rstrip().split(" ")
        
        # 回傳最後一個字的長度
        return len(s[-1])

s58 = Solution()
a = s58.lengthOfLastWord("   fly me   to   the moon  ")
print(a)