class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        dic = {}

        for i in m:
            dic[i] = dic.get(i,0)+1
        for j in r:
            if j not in dic or dic[j]<=0:
                return False
            dic[j]-=1
        print(dic)
        return True