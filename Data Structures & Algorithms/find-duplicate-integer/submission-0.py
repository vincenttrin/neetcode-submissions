class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        last = -1
        for num in nums:
            if num == last:
                return num
            last = num
        