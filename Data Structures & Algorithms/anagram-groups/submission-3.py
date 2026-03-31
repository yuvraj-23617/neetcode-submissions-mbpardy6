class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        
        for each in strs:
            a = "".join(sorted((each)))
            if a not in dictt:
                dictt[a] = []
            dictt[a].append(each)
        return list(dictt.values())