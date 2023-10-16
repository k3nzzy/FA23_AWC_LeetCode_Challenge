class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack= [] #[[temp, index], [temp, index], ... ] //to store the date difference once the higher temperature is found when iterating each day
        ans = [0] * len(temperatures) #initialize 0 as if there is no warmer temperature in the future so we don't wait each day
        
        for idx, temp in enumerate(temperatures): #iterate over the given temperatures list
            while stack and temp > stack[-1][0]: #comparing with the pair of [max temp, day of max temp]
                stack_index = stack.pop()       #IF the temperature for each iteration is bigger(warmer) i.e., there is a warmer day after
                ans[stack_index[-1]] = (idx - stack_index[-1]) #append the date difference from the warmer date for the date as an index
            stack.append([temp, idx]) #no matter what, store [temp, index(date)] in stack

        return ans #return list of how many days you have to wait for the warmer temperature