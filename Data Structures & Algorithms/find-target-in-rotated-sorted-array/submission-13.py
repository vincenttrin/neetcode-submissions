class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums)== 1 and nums[0] == target: return 0
        while l < r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[l] == target: return l
            if nums[r] == target: return r
             # 4 cases
            # no rotate point in the range btw l,m and m,r
            if nums[l] < target and target < nums[m]:
                r = m - 1
            elif nums[m] < target and target < nums[r]:
                l = m + 1
            # rotate point in the range
            elif nums[l] > nums[m]:
                r = m - 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                return -1

        return -1