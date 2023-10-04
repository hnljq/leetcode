from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		right = len(nums) -1
		left = 0
		while left <= right:
			m = (left + right) // 2
			if nums[m] == target:
				return m
			elif nums[m] < target:
				left = m +1
			else:
				right = m -1
		return -1


if __name__ == '__main__':
	# nums = [-1,0,3,5,9,12]
	# target = 9
	nums = [5]
	target = 5
	s = Solution()
	print(s.search(nums, target))
	for i, v in enumerate