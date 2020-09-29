# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        判断回文数，转化为字符串，判断其与其颠倒后的对象是否相同
        :param x: 输入数
        :return:
        """
        s = str(x)
        return s == s[::-1]

test = Solution()
print(test.isPalindrome(1123))
