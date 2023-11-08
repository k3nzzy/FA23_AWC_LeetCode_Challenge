class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        profit = [nums[0], nums[1]]

        for i in range(2, len(nums)):
            profit.append(profit[i - 2] + nums[i])
        
        return max(profit[-1], profit[-2])
