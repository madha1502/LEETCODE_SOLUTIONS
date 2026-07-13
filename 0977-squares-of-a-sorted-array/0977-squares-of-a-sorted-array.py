import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = np.array(nums)
        arr = arr*arr
        arr = np.sort(arr)
        return arr.tolist()