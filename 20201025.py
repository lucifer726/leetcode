class Solution:
    def isValid(self, s: str) -> bool:
        # 如果字符串个数为奇数，直接返回false
        if len(s) % 2 == 1:
            return False

        # 创建字典用于存储括号
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        # 创建栈，用于存储输入的括号
        stack = list()
        # 遍历输入的字符串
        for ch in s:
            # 如果ch属于pairs的key
            if ch in pairs:
                # 如果栈为空或者栈顶元素不是右括号（key）所对应的左括号（value），返回false
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # 否则弹出栈顶元素
                stack.pop()
            else:
                # 如果不属于pairs的key，则存入stack
                stack.append(ch)
        # 返回stack是否为空
        return not stack

if __name__ == '__main__':
    A = Solution()
    print(A.isValid("([{}])"))