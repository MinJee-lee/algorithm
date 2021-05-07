class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        x = []
        for i in range(len(index)):
            x.insert(index[i], nums[i]) 
        return x