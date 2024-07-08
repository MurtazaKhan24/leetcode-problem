class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minProfit = prices[0]
        for i in prices:
            if i < minProfit:
                minProfit = i
            res = max(res, i - minProfit)
        return res