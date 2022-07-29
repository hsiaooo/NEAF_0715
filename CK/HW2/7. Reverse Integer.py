class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        rev_x = int(str_x[::-1])
        if -2**31 <= rev_x < 2**31:
            if x >= 0:
                return rev_x
            else:
                return -rev_x
        else:
            return 0