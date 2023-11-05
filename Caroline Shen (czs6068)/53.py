class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum, currentSum = nums[0], 0 

        for num in nums:
            if currentSum < 0:
                currentSum = 0
        
            currentSum += num

            maxSum = max(maxSum, currentSum)


        return maxSum