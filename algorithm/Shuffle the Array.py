class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i]) # 첫번째 값
            result.append(nums[i+n]) #두번째 값은 n만큼 더한 위치
        return result