# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        printNodes(l1)
        printNodes(l2)
        if l1 is None and l2 is None:
            return None
        a = 0
        b = 0
        l11 = l1
        l21 = l2
        if l1 is not None:
            a = l1.val
            l11 = l1.next
        if l2 is not None:
            b = l2.val
            l21 = l2.next
        c = ListNode(a + b)
        c.next = self.addTwoNumbers(l11, l21)

        e = c
        while e.val > 9:
            e.val -=10
            if e.next is None:
                e.next = ListNode(1)
                break
            else:
                e.next.val += 1
                e = e.next
        return c

    def recursion(self, index, l11: ListNode, l12: ListNode):
        if index == 0:
            return


def size(l: ListNode):
    if l is None:
        return 0
    s = 1
    while l.next is not None:
        l = l.next
        s += 1
    return s


def printNodes(l: ListNode):
    while l is not None:
        print(str(l.val) + ' -> ', end='')
        l = l.next
    print('---------')

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    # l1.next = l2
    # l2.next = l3
    r1 = ListNode(9)
    r2 = ListNode(9)
    r1.next = r2
    # printNodes(r1)
    s = Solution()
    printNodes(s.addTwoNumbers(l1, r1))