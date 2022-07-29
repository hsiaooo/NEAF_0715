class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ans = target - nums[i]  # 得出另一個答案
            for j in range(i+1, len(nums)):
                if ans == nums[j]:   # 看是否在list裡面
                    return [i, j]