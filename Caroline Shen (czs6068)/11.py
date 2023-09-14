class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right, area = 0, len(height) - 1, 0 

        while left < right:

            # compute the area and choose the max
            area = max(area, ((right - left) * min(height[left], height[right])))

            # move pointer for smaller height

            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        
        return area


