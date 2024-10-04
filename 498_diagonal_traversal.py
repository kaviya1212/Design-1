class Solution:
    # time complexity O(n*m)
    # space complexity O(n*m)
    # calculate the number of diagonals and traverse them one by one. For each diagonal, it collects elements in an intermediate list, reversing the order of elements when the diagonal index is even, and appending the result to the final result list.
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        result = []

        diagonal = rows + cols - 1

        for d in range(diagonal):

            intermediate = []

            if d < cols:
                row, col = 0, d
            else:
                row, col = d - cols + 1, cols-1

            while row < rows and col >= 0:
                intermediate.append(mat[row][col])
                row += 1
                col -= 1

            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return(result)