class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0

        for i in prices:
            min_buy = min(min_buy, i)
            today_profit = i - min_buy
            max_profit = max(max_profit, today_profit)
        return max_profit
