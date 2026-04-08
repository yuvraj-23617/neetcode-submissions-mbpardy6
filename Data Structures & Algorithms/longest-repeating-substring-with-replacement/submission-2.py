class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = ""
        lis = []
        
        for i in s:
            st = st + i
            
            while len(st) - max(st.count(c) for c in set(st)) > k:
                st = st[1:]
                
            lis.append(len(st))
            
        return max(lis)