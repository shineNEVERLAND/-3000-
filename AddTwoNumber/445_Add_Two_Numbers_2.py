# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        i = len(s1) - 1
        j = len(s2) - 1
        middle = 0
        result = []
        while i >= 0 or j >= 0 or middle:
            tmp = middle
            if i >= 0:
                tmp += s1[i]
                i -= 1
            if j >= 0:
                tmp += s2[j]
                j -= 1
            result.append(tmp % 10)
            middle = tmp / 10
        r = result[::-1]
        head = p = ListNode(0)
        for item in r:
            p.next = ListNode(item)
            p = p.next
        return head.next



