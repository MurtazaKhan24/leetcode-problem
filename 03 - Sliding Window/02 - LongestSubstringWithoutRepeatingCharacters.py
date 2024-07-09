class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = set()
        maxLen = 0
        l = 0
        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[i])
            maxLen = max(maxLen, i - l + 1)
        return maxLen