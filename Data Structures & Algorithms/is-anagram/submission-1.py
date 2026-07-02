class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            s, t = t, s
        for ch in s:
            idx = t.find(ch)
            if idx == -1:
                return False
            elif s.count(ch) != t.count(ch):
                return False
        return True