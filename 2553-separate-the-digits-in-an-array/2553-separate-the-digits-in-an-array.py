class Solution:
    def separateDigits(self, li: List[int]) -> List[int]:
        words = ""
        for i in li:
            words+=str(i)
        chars = [char for word in words for char in word]
        anss = list(map(int, chars))
        return anss