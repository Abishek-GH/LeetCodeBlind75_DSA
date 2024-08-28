# Solution 1 (Not Recommended)
# General Trial
'''
class Solution:
    def maxProfit(self, prices):
        temp = prices
        profit = 0
        if sorted(temp, reverse=True) == prices:
            profit = 0
        else:
            for i in range (len(prices)-1):
                if prices[i] < prices[i+1]:
                    profit = prices[i+1] - prices[i]  
                    for j in range(i, len(prices) -1):
                        currentProfit = prices[j+1] - prices[i]
                        if currentProfit > profit:
                            profit = currentProfit 
                else: 
                    continue

        return profit

prices = [7,1,5,3,6,4]
solution = Solution()
result = solution.maxProfit(prices)
print(result)
'''
# Solution 2
# Approach --> DP
# Time Complexity --> O(n)
class Solution:
    def maxProfit(self, prices):
        minimumValue = prices[0]
        maxProfit = 0
        n = len(maxProfit)
        for i in range (n):
            cost = prices[i] - minimumValue
            maxProfit = max(maxProfit, cost)
            minimumValue = min(minimumValue, prices[i])

        return maxProfit
        

prices = [7,1,5,3,6,4]
solution = Solution()
result = solution.maxProfit(prices)
print(result)