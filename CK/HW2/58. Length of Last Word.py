class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s[-1] == " ":  # 將後面空格刪除
            s = s[:-1]
        word = s.split()  # 用空格分割成list
        return len(word[-1])