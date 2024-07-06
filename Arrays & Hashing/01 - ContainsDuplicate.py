class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDup = set()
        for i in range(len(nums)):
            if nums[i] in isDup:
                return True
            isDup.add(nums[i])

        return False