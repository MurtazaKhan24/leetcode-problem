class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while l < r:
            mid = int((l + r) // 2)
            if target < nums[mid]:
                r -= 1
            elif target > nums[mid]:
                l += 1
            else:
                return mid
        return -1