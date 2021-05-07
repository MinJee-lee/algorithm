class Solution:
    def isValid(self, s: str) -> bool:
                
        stack = []
        
        brackets={'}':'{',
                  ')':'(',
                  ']':'['} 
           
        if len(s)<2:
            return False
        
        for bracket in s:
            if bracket in brackets.values(): 
                stack.append(bracket)
            
            else:
                
                if not stack or brackets[bracket] != stack.pop():
                    return False
        if stack: 
            return False
        return True