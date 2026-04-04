class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for x in range(len(nums)):
            i = nums[x]
            for y in range(x + 1, len(nums)):
                j = nums[y]
                k = 0 - (i + j)

                if k in counts:
                    n = [i, j, k]
                    n.sort()
                    if (
                        n.count(i) <= counts.get(i, 0) and
                        n.count(j) <= counts.get(j, 0) and
                        n.count(k) <= counts.get(k, 0)
                    ):
                        final.append(tuple(n))
        final = list(set(final))

        return [list(x) for x in final]