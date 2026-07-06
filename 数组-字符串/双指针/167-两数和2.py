from typing import List

class Solution:
    """数组有序,两个数满足什么制约条件，双指针"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Hash"""
        cache = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in cache:
                return [cache[complement] + 1, i + 1]
            cache[num] = i

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """常量空间解法 双指针"""
        left = 0
        right =len(numbers) - 1
        while left != right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1

