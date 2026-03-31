class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(set(nums)) == 1:
            return 1
        elif nums == []:
            return 0 
        else:
            n = 1
            l = 1
            el = []
            for i in nums:
                while i + n in nums:
                    l = l + 1
                    n = n + 1
                    el.append(l)
                else:
                    n = 1
                    l = 1
                    continue
            if el == []:
                return 1
            else:
                return max(el)