class Solution:
    # time complexity: o(log n)
    # space complexity: o(1)
    # Binary search is used to search for the element both the left and right to find the first and last position of target.
    #It searches twice: once for the leftmost occurrence and once for the rightmost, returning the indices of both. 
    #If the target is found, the indices are returned; otherwise, it returns [-1, -1].
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, side):
            low = 0
            high = len(nums) - 1
            index = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    high = mid -1
                elif nums[mid] < target:
                    low = low + 1
                else: 
                    index = mid
                    if side == 'left':
                        high = high - 1
                    else:
                        low = low + 1

            return index
        
        left = binarySearch(nums, target, 'left')
        right = binarySearch(nums, target, 'right')

        return [left, right]
