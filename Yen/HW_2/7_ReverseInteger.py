class Solution:
    def reverse(self, x: int) -> int:

        # 轉成字串形式，並翻轉
        x_str = str(x)[::-1]

        # 如果是 x < 0，加負號
        if x < 0:
            x_str = "-" + x_str[:-1]

        # 確認 x 的範圍
        if int(x_str) > (2 ** 31 - 1) or int(x_str) < (- 2 ** 31):
            x_str = 0

        return int(x_str)

s7 = Solution()
a = s7.reverse(-123)
print(a)