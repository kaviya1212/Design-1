class Solution:
    #time complexity = o(logn)
    #space complexity = o(1)
    #minimum is set to positive infinity and using binary search compare minimum with the first element, last element and and mid element with the minimum based on which is the lesser value among them. 
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        minimum = float('inf')

        while low <= high:
            mid = (low+high)//2
            if nums[low] <= nums[high]:
                minimum = min(minimum, nums[low])
                break
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])
                low = mid+1
            else:
                minimum = min(minimum, nums[mid])
                high = mid-1
        return minimum