import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sss = re.sub(r'[^a-zA-Z0-9]','', s)
        ss = sss.lower()
        s_ns = ss.replace(" ", "")
        s_rv = s_ns[::-1]
        return s_rv == s_ns