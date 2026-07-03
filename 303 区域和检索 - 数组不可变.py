from typing import List

class NumArray(object):
    """前缀和 O(N), 递归中。。。，需要对数组的区间进行大量操作。连续子数组，和，区间，平均数。"""
    def __init__(self, nums:List[int]):
        self.preSum = [0]* (len(nums) + 1)
        for i in range(len(nums)):
            self.preSum[i+1] = self.preSum[i] + nums[i]
        
    def sumRange(self, left, right):
        return self.preSum[right+1] - self.preSum[left]
        

      


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)