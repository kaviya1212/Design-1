class Solution:
    # time complexity O(n)
    # space complexity O(1)
    # get the length of the list and create an empty list to store the missing numbers. convert the list to set to eliminate duplicates and to make look up time O(1). add the numbers that are not in the set from 1 to the length of nums.
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        num_set = set(nums)

        for i in range(1,n+1):
            if i not in num_set:
                result.append(i)

        return(result)

        