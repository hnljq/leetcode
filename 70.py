"""爬楼梯"""


class Solution:
	def climbStairs(self, n: int) -> int:
		a = 0
		b = 0
		c = 1
		for i in range(1, n+1):
			a = b
			b = c
			c = a+b
		return c


if __name__ == '__main__':
	n = 5
	s = Solution()
	print(s.climbStairs(n))
