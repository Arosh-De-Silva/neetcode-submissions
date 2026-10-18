class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    middle = left + (right - left) // 2
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        return False