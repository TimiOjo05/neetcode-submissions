class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for y in range(i + 1, len(prices)):
                profitT = prices[y] - prices[i]
                if profitT > profit:
                    profit = profitT
        return profit

                 
            