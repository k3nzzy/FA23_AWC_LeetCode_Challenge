class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        maxLen = 0

        # use set (faster for removing)
        currentChars = set()

        while right < len(s):
            
            # if duplicate, move left pointer
            while s[right] in currentChars: 
                currentChars.remove(s[left])
                left += 1
            
            # add right to char set, update maxLen
            currentChars.add(s[right])
            maxLen = max(maxLen, (right - left) + 1)

            right += 1

        return maxLen