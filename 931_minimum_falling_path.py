class Solution:
    # time complexity O(n^2)
    # space complexity O(1)
    # calculate and replace the elements from the second row with the minimum from the row before in the left, middle or right till the last row. Return the minimum from the last row.
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        for r in range(1, n):
            for c in range(n):
                mid = matrix[r-1][c]
                left = matrix[r-1][c-1] if c > 0 else float('inf')
                right = matrix[r-1][c+1] if c < n-1 else float('inf')
                minimum = min(left, mid, right)
                matrix[r][c] += minimum

        return(min(matrix[-1]))