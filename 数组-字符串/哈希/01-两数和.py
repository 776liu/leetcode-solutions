from typing import List

class Solution:
    """发现需要重复遍历时，需要记忆已经遍历过很多遍的元素时。使用哈希"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """暴力拆 平方复杂度N^2(两层循环)"""
        for i, item in enumerate(nums):
            for j in range(i + 1, len(nums)):
                post = nums[j]
                if item + post == target:
                    return [i, j]
                
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """哈希表"""
        # 制表
        cache = {}
        for i, imtem in enumerate(nums):
            cache[imtem] = i
        
        for i, item in enumerate(nums):
            orther = target - item
            # 要注意，如果orther和item相同，那么就会出现重复的情况，所以要判断一下
            if orther in cache and cache[orther] != i:
                return [i, cache[orther]]
    
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """哈希表优化"""
        # 遍历之后制表
        cache = {}
        for i, item in enumerate(nums):
            orther = target - item
            if orther in cache:
                return [cache[orther], i]
            cache[item] = i
        