class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countofnums = []
        for items in nums:
            countofnums.append(nums.count(items))
        countofnums.sort(reverse = True)
        dictt = {}
        for each in nums:
            for each2 in countofnums:
                if nums.count(each) == each2:
                    dictt.update({each:each2})
        result = sorted(dictt, key=dictt.get, reverse=True)[:k]
        return result