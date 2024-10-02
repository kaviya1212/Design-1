class Solution:
    # time complexity O(n)
    # space complexity O(n)
    # It keeps a running total (prefix_sum) and tracks the frequency of each sum in a dictionary (prefix_sum_count). For each element, if the difference (prefix_sum - k) exists in the dictionary, it indicates that a subarray summing to k has been found, and the count is updated accordingly.
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0:1}

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]

            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1
        return count