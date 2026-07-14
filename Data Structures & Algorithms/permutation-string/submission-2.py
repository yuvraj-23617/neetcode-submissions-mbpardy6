class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        first = 0
        last = n-1
        lsts1 = list(s1)
        lsts2 = list(s2)
        for i in range(len(lsts2) - len(lsts1) + 1):
            if sorted(lsts2[first : last + 1]) == sorted(lsts1):
                return True
            else:
                first = first + 1
                last = last + 1
        return False