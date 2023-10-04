from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a, b, c = 0, len(nums)-1, len(nums)-1
        res = [1] * len(nums)
        while a < b:
            if nums[a] ** 2 <= nums[b] **2:
                res[c] = nums[b]**2
                b-=1
            else:
                res[c] = nums[a]**2
                a+=1
            c -=1
        return res

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    s = Solution()
    print(s.sortedSquares(nums))