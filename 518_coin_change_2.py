class Solution:
    # time complexity: O(n*m)
    # space complexity: O(m)
    # dp[i] represents the number of ways to make the amount i, initializing dp[0] to 1 since there is one way to create the amount 0 (using no coins). For each coin, it updates the dp array to count the combinations for amounts from the coin value up to the target amount.
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = dp[i] + dp[i-coin]

        return dp[-1]