# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2024年04月09日
"""
# Leetcode 2 两数相加

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = 0
        n1, n2 = l1, l2
        head = ListNode()
        node = head
        while n1 or n2 or cur:
            if n1:
                cur += n1.val
                n1 = n1.next
            if n2:
                cur += n2.val
                n2 = n2.next
            node.next = ListNode(cur % 10)
            node = node.next
            cur //= 10
        return head.next
