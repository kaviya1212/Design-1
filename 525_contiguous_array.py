class Solution:
    # time complexity O(n)
    # space complexity O(n)
    # count the number of 0's and 1's in the given array. calculate the difference in 0's and 1's and add it as key to the dictionary and index as value. 
    # if the count of 1's and 0's are the same add the values to count. else update count with the longest balanced subarray of 0s and 1s. 
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        one = 0
        zero = 0
        diff_index = {}
        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                one += 1
            
            if (zero - one) not in diff_index:
                diff_index[zero-one] = i

            if one == zero:
                count = one+zero
            else:
                idx = diff_index[zero-one]
                count = max(count, i - idx)

        return count
