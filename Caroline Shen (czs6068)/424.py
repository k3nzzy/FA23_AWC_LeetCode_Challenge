class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxFreq = 0, 0
        freq = {}

        for right in range(len(s)):
            
            # update the frequency count within window
            freq[s[right]] = s[left:right + 1].count(s[right])
            
            # update the max frequency
            maxFreq = max(maxFreq, freq[s[right]])
            
            # if not within k, then move window left
            if (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
        
        # return size of window
        return right - left + 1
