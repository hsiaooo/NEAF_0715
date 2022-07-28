class Solution:
    def climbStairs(self, n):
        n_list = [0] * n
        for i in range(n):
            if i == 0 or i == 1:
                n_list[i] = i + 1
            else:
                n_list[i] = n_list[i - 1] + n_list[i - 2]
        return n_list


s70 = Solution()
a = s70.climbStairs(9)
print(a)

  