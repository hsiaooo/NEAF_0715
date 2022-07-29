class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        
        # 創建一個 dict，dict = {數字: 位置}
        numMap = {}
        
        for i in range(len(nums)):
            
            # 如果 target - 數字 在 numMap 中，回傳[numMap.get(target - nums[i]), i]
            if numMap.__contains__(target - nums[i]):
                return [numMap.get(target - nums[i]), i]
            else:
                numMap[nums[i]] = i

s1 = Solution()
a = s1.twoSum([2, 7, 11, 15], 9)
print(a)