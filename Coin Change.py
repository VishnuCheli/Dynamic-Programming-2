#Time Complexity:: Average: O(n*m)
#Space Complexity:: O(n) where n is the maximum number of elements.Using a new array.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #rows: len(columns)+1
        #columns: target amount
        dp = [[0 for _ in range(amount+1)] for s in range(len(coins)+1)]
        
        for i in range(1,amount+1):
            dp[0][i] = amount + 1
            
        for i in range(1, len(coins)+1):
            for j in range(amount+1):
                if j<coins[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])
                    
        if dp[-1][-1] == amount+1:
            return -1
        
        return dp[-1][-1]