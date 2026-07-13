class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        双指针消消乐 最后无剩余则True
        先判断有无相邻的，然后替换为空

        但是复杂度为N-> 栈
        开始遍历入栈。。若遇到相邻的配对括号则出栈
        遇到左元素入栈，遇到右元素弹出比较。
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in {"(", "{", "["}:
                stack.append(char)
            else:
                # 出栈前先判断
                if not stack:
                    return False
                
                top_ele = stack.pop()
                # 映射关系，直接使用哈希
                if mapping[char] != top_ele:
                    return False
        
        if not stack:
            return True
        else: 
            return False


        