class Solution:
    #time complexity = O(log n)
    #space complexity = O(1)
    #Used Binary search. check if the mid element is the first element or the last element.
    # if its the first element check whether the element after it is less than and for the last element check the element before it to handle edge cases.
    # If the element before mid is greater, we search the left half, as the peak must be in that direction. Otherwise, we search the right half.
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if (mid == 0 or nums[mid]>nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1