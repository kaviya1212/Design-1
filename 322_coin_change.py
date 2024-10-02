class Solution:
    #time complecity: O(n^2)
    #space complexity: O(n)
    # A dp array is initialized where where stores the minimum coins needed for amount x, and iterates over each coin, updating dp[x] by checking if using the current coin results in a smaller count. If the amount can't be made, it returns -1; otherwise, it returns dp[amount].
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make 0 amount
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1