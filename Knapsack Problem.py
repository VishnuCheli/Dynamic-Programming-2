#Time Complexity:: Average: O(n^2)- traversing  a 2D array
#Space Complexity:: O(n) - Using an extra 2D array 
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
#knapsack
def knapSack(val,wt,C,n):
    dp=[[0 for _ in range(C+1)]for s in range(n+1)] #creating a 2D array
    
    for i in range(1,n+1): #rows columns
        for j in range(C+1): #
            if j < wt[i-1]: #not considering wt[i-1] till bag capacity is equal to wt[i-1]
                dp[i][j] = dp[i-1][j-1] #element from previous row is copied
            else:
                dp[i][j]= max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]]) #driving function finds the max that can fit in the bag out of the items
                
    return dp[-1][-1]
                

#Driver Code
val = [1,4,5,7] #value array
wt = [1,3,4,5] #weight of each item
C = 7 #bag capacity
n = len(val)
print(knapSack(wt,val,C,n))