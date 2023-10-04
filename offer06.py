from typing import List


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


# class Solution:
# 	def reversePrint(self, head: ListNode) -> List[int]:
# 		print(head)
# 		return self.reversePrint(head.next) + [head.val] if head else []

class Solution:
	def reversePrint(self, head: ListNode) -> List[int]:
		stack = []
		while head:
			stack.append(head.val)
			head = head.next
		return stack[::-1]


if __name__ == '__main__':
	n1 = ListNode(1)
	n2 = ListNode(3)
	n3 = ListNode(2)
	n1.next = n2
	n2.next = n3
	s = Solution()
	print(s.reversePrint(n1))
