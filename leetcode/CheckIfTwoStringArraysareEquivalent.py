class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x1 = []
        x2 = []
        
        for y in word1:
            for char in y:
                x1.append(char)
                
        for y in word2:
            for char in y:
                x2.append(char)
                
        return x1 == x2