class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 0
        profit = 0
        for i in range(len(prices)):
            for y in range(i + 1, len(prices)):
                profitT = prices[y] - prices[i]
                if profitT > profit:
                    profit = profitT
        return profit

                 
            