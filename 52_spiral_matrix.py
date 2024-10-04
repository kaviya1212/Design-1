class Solution:
    # time complexity O(n*m)
    # space complexity O(n*m)
    # create an empty list - result. while the matrix is not empty pop and add the first row to the result, then remove and add the last element of each row.
    # next reverse the last row. Then finally reverse and add the last element of the list. Repeat till the matrix is empty.
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix: 
            result += matrix.pop(0) 

            if matrix and matrix[0]: 
                for row in matrix:
                    result.append(row.pop())

            if matrix:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result