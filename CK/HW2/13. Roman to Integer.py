class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000,
                'IV' : 4,
                'IX' : 9,
                'XL' : 40,
                'XC' : 90,
                'CD' : 400,
                'CM' : 900}
        sum = 0
        sp = len(s)
        while sp > 0:
            if sp > 1:                        # 從尾巴搜尋，先搜尋兩個字，如果沒有才會搜尋一個字
                if s[sp-2:sp] in dict:
                    sum += dict[s[sp-2:sp]]
                    sp -= 2
                else:
                    sum += dict[s[sp-1]]
                    sp -= 1
            else:
                sum += dict[s[sp-1]]
                sp -= 1
        return sum
    
    '''
    str     A  B  C  D  E
    
    index   0  1  2  3  4  5 ->sp(剩下未轉換的字數)
                               
    '''