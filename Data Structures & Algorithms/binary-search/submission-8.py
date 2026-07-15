class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = len(nums) // 2
        for _ in nums:
            if nums[int(middle)] == target:
                return int(middle)
            elif nums[int(middle)] > target:
                end = middle - 1
                middle = (start + end) // 2
            elif nums[int(middle)] < target:
                start = middle + 1
                middle = (start + end) // 2
        return -1