class Solution:
    def isvow(self, ch):
        return ch in "aeiouAEIOU"

    def reverseVowels(self, a: str) -> str:

        s = list(a)

        vow = []
        cons = []

        for i in a:
            if self.isvow(i):
                vow.append(i)
            else:
                cons.append(i)

        vow = vow[::-1]

        ans = []

        j = 0
        k = 0

        for i in s:
            if self.isvow(i):
                ans.append(vow[j])
                j += 1
            else:
                ans.append(cons[k])
                k += 1

        return "".join(ans)