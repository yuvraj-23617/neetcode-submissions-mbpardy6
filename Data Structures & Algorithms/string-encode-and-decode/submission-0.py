class Solution:
    def encode(self, strs: List[str]) -> str:
        stng = ""
        for i in strs:
            stng = stng + str(len(i)) + "#" + i
        return stng

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            
            word = s[i : i + length]
            res.append(word)
            
            i = i + length
            
        return res
