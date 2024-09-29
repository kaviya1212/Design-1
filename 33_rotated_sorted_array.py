class Solution:

    # time complexity = o(log n)
    # space complexity = o(1)
    # The code uses modified binary search algorithm. As the array is rotated it finds correctly ordered halves of the array and then finds the target.

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]: 
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]: 
                    low = mid + 1
                else:
                    high = mid - 1
        return -1