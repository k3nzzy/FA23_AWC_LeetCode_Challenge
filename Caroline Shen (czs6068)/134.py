class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        result = 0
        totalSurplus, currentSurplus = 0, 0

        for i in range(len(gas)):
            totalSurplus += gas[i] - cost[i]

            # tracking surplus for current sequence
            currentSurplus += gas[i] - cost[i]

            if currentSurplus < 0:
                currentSurplus = 0
                result = i + 1
        
        if totalSurplus < 0:
            return -1
        
        return result