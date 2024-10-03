class Solution:
    # time complexity O(n)
    # space complexity O(n)
    # dp[i] represents the maximum amount that can be robbed from the first i houses, calculating it by choosing the maximum of either robbing the current house (adding its value to the amount robbed two houses back) or skipping it (taking the amount robbed from the previous house).
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
     
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]