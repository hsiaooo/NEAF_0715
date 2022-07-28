class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        # 從 list 變成 str 形式
        d_str = str()
        for i in digits:
            d_str += str(i)
            
        # + 1    
        d_str = str(int(d_str) + 1)
        
        # 從 str 變成 list 形式
        d_list = [0] * len(d_str)
        for i in range(len(d_str)):
            d_list[i] = int(d_str[i])
            
        return(d_list)

s66 = Solution()
a = s66.plusOne([4,3,2,2])
print(a)