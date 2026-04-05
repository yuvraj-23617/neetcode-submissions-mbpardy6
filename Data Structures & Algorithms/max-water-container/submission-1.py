class Solution:
    def maxArea(self, heights: List[int]) -> int:
        listt = []
        f = 0
        l = len(heights) - 1
        for i in heights:
            dis = abs(f - l)
            water = dis * min(heights[f], heights[l])
            listt.append(water)
            if heights[f] <= heights[l]:
                f = f + 1
            else:
                l = l - 1
        return max(listt)