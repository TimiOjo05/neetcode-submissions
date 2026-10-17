class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dif = 0
        lowestday = 100
        for i in range(len(prices)):
            if prices[i] < lowestday:
                lowestday = prices[i]
            temp = prices[i] - lowestday
            if temp > dif:
                dif = temp
        return dif
            