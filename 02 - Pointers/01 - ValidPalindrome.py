class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s.replace(" ", "")
        old = list(s)
        new = []
        for i in old:
            if i.isalnum():
                new += i
        l,r = 0, len(new) - 1
        while l < r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1
        return True