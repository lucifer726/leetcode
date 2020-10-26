class ListNode(object):  # 定义一个Node的类
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def getNewChart(self, List):  # 将一个列表转换成链表
        if List:
            Node = ListNode(List.pop(0))
            Node.next = self.getNewChart(List)
            return Node

    def Merge(self, pHead1, pHead2):  # 递归实现链表合并
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.value <= pHead2.value:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


def main():
    List1 = [1, 2, 4, 6]
    List2 = [1, 3, 5]
    testnode1 = Solution().getNewChart(List1)
    testnode2 = Solution().getNewChart(List2)
    testnode = Solution().Merge(testnode1, testnode2)

    while testnode:
        print(testnode.value, end=' ')
        testnode = testnode.next


if __name__ == '__main__':
    main()
