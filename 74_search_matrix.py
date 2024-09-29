class Solution:

    # time complexity = o(log(m*n))
    # space complexity = o(1)
    # The code uses binary search algorithm. The first while loop (Binary search) finds which row the target element could be in as the matrix is in order.
    # The second while loop (binary search) tries to find the element in the particular row. If present returns true else returns false.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2 

            #middle row
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][0] > target:
                high = mid - 1 
            else:
                low = mid + 1
        
        row = (low + high) // 2 #row the target could be in
        
        left = 0
        right = len(matrix[row]) - 1 #columns

        while left <= right:
            mid = (left + right) // 2 

            if matrix[row][mid] == target: 
                return True
            elif matrix[row][mid] > target:
                right = mid - 1   
            else:
                left = mid + 1
        return False