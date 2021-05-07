def solution(numbers, target):
    def recursion(nums, cur, tar):
        if not nums:
            if cur == tar:
                return 1
            else:
                return 0
        thisNum = nums.pop(0)
        return recursion(nums[:], cur+thisNum, tar) + recursion(nums[:], cur-thisNum, tar)
    return recursion(numbers, 0, target)