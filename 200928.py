# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
class Solution:
    def reverse_better(self, x: int) -> int:
        y, res = abs(x), 0
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res



if __name__ == '__main__':
    a = Solution()
    x = int(input("请输入："))
    print(a.reverse_better(x))

