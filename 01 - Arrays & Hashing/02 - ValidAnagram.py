class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        listS = list(s)
        for i in range(len(t)):
            if t[i] not in listS:
                return False
            elif t[i] in listS:
                listS.remove(t[i])
        
        return True