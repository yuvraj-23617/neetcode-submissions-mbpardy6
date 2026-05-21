class Solution:
    def calresult (self, newlist, nums: List[int]) -> List[int]:
        a = 1
        b = 1
        for i in nums:
            a = a * i
        for k in nums:
            if k == 0:
                continue
            else:
                b = b * k
        for j in nums:
            if j != 0:
                newlist.append(int(a/j))
            elif j == 0:
                if nums.count(0) > 1:
                    newlist.append(0)
                else:
                    newlist.append(b)
        return newlist


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newlist = []
        return self.calresult(newlist, nums)