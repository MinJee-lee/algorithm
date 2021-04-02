import collections

#1
class Solution:
    
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]               
            
        return nums

#2
class Solution1:
    
    def runningSum(self, nums: List[int]) -> List[int]:
    
        i = []
        mid_sum = collections.defaultdict(int)
        
        for index, value in enumerate(nums): #반복문 사용 시 몇 번째 반복문인지 확인
            current_sum = mid_sum[index-1] + value # 인덱싱하면 기본값 나옴
            i.append(current_sum)
            mid_sum.update({index:current_sum})
                         
        return i




