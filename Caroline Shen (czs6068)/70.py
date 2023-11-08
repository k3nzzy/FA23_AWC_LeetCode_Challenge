class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        elif n == 2:
            return 2
        
        result = [0] * (n + 1)
        result[0] = 1   #number ways to get to 0th step
        result[1] = 1   #nuber of ways to get to 1st step

        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        
        return result[n]
    
        