class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # set buy to first index
        buy = prices[0]

        # iterate through the list
        for sell in iter(prices):
            # check if profitable and if profit is max
            if sell > buy and sell - buy > profit:
                profit = sell - buy
            # if not profitable or maximum profit, set buy to new value
            elif sell < buy:
                buy = sell 
        return profit 
