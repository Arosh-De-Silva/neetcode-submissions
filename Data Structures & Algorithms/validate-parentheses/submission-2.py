class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbDict = {")": "(", "]": "[", "}": "{"}
        for symbol in s:
            if symbol in symbDict.values():
                stack.append(symbol)
            elif not stack:
                return False
            elif stack[-1] == symbDict[symbol]:
                    stack.pop()
            else:
                return False
        return not stack