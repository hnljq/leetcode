from typing import List


class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		for i in nums:
			result = 0
			for j in nums[1:]:
				result = i + j
				if


