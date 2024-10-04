class Solution:
    # space complexity O(n)
    # time complexity O(n)
    # The index and the value from nums is stored in a dictionary. If the difference between target and number exsist in the dictionary the index of the difference and the current index is returned. If no match is available an empty list is returned.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []