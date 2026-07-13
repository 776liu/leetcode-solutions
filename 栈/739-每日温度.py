class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]

        单调栈：当前值需要以后的信息时(更高，更小)，增援未来
        """
        n = len(temperatures)
        stack = [0] * n
        answer = []

        for i in range(n):
            cur_tem = temperatures[i]
            while stack and cur_tem > temperatures[stack[-1]]:
                pre_index = stack.pop()
                stack[pre_index] = i - pre_index

            stack.append(i)

        return answer