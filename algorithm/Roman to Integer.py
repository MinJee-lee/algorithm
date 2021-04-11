class Solution:
    def romanToInt(self, s: str) -> int:
   
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        x = len(s)
        result = dic[s[x-1]]
        for i in range(x-1,0,-1):
            cur = dic[s[i]]
            y = dic[s[i-1]]
            result += y if y >= cur else -y
        return result 