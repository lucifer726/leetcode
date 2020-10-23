#  最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        """
        首先判断列表长度，将两两的匹配得到的结果，与之后的字符串进行比较
        :param strs:
        :return: 最长公共前缀
        """
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        """
        依次比较两个字符串，返回最长相似序列
        :param str1:
        :param str2:
        :return:
        """
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


if __name__ == '__main__':
    A = Solution()
    print(A.longestCommonPrefix(["flower", "flow", "flight"]))
