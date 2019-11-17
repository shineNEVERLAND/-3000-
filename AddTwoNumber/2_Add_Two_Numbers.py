# coding: utf-8


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
        r = head = ListNode(0)  # 头指针初始化为0，为了方便Python表示链表结构(其实主要是这个垃圾数据结构的构造函数需要初始值。垃圾)
        middle = 0
        while l1 or l2 or middle:  # or middle这个case：[5]、[5]这个case的输出是: [0, 1]
            if l1:
                middle += l1.val
                l1 = l1.next
            if l2:
                middle += l2.val
                l2 = l2.next
            tmp = ListNode(middle % 10)
            r.next = tmp
            r = r.next
            middle /= 10
        return head.next