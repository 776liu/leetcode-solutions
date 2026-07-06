class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        不能通过滑动窗口做。。因为数组不为正整数，k值也不一定为整数，数组不单调。。
        求和--前缀和
        """

        count = 0
        preSum = [0]*(len(nums)+ 1)

        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]

        cache = {}
        for i, itme in enumerate(preSum):
            other = itme - k 
            if other in cache:
                count += cache[other]
            cache[itme] = cache.get(itme, 0) + 1

        return count
            

