class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for i in numbers:
            if (target - i) in numbers and numbers.index(i) != numbers.index(target - i):
                output.append(numbers.index(i)+1)
                output.append(numbers.index(target - i)+1)
                break
        return output