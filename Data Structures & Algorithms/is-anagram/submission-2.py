class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s);
        list_t = list(t);
     
        for i in set(list_s):
            if(list_s.count(i) == list_t.count(i)):
                k = 0;
                for i in set(list_s):
                    for j in set(list_t):
                        if j == i:
                            k += 1
                        else:
                            continue
                if(len(list_s)) == len(list_t):
                    if(len(set(list_s)) == len(set(list_t))):
                        if k == len(set(list_s)):
                            return True;
        return False;