class Solution:
    def separateDigits(self, li: List[int]) -> List[int]:
        words = ""
        for i in li:
            words+=str(i)
        chars = []
        for i in words:
            chars.append(i)
        anss = list(map(int, chars))
        return anss