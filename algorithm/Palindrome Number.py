class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0 : return False 
        
        else: 
            if x == int(str(x)[::-1]): # String 으로 변환 후 셔플
                
                return True # 같으면
            else:    
                return False # 다르면 