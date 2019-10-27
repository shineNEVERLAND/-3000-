class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = head = ListNode(0)
        middle = 0
        while l1 or l2 or middle:
            tmp = 0
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            tmp += middle
            r.next = ListNode(tmp % 10)
            r = r.next
            middle = tmp / 10
        return head.next
