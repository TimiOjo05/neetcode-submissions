class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                temp = prices[j] - prices[i]
                if temp > dif:
                    dif = temp
        return dif