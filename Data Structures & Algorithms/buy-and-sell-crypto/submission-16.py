class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0

        for i in prices:
            low = min(low, i)
            today_profit = i - low
            profit = max(profit, today_profit)

        return profit