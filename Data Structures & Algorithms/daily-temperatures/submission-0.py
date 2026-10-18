class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        stack = []
        for currIndex in range(len(temperatures)):
            while stack and temperatures[currIndex] > temperatures[stack[-1]]:
                prevDayIndex = stack.pop()
                result[prevDayIndex] = currIndex - prevDayIndex
            stack.append(currIndex)
        return result