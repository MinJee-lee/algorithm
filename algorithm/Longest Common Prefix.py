class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = ""
        if not strs :
            return x
        y = min(strs, key=len)
        for i in range(len(y)) :
            cur = strs[0][i]
            for j in range(1, len(strs)) :
                if strs[j][i] != cur :
                    return x
            x = x + cur

        return ( x )



