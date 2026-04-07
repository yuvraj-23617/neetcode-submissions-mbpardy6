class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ""
        emp_s = left
        listt = []
        for k, i in enumerate(s):
            if i not in emp_s:
                emp_s = emp_s + i
            else:
                listt.append(len(emp_s))
                emp_s = emp_s[emp_s.index(i)+1:] + i
        listt.append(len(emp_s))
        return max(listt, default = 0)
