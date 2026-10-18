class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        leftP = 0
        rightP = len(s) - 1
        while leftP < rightP:
            if s[leftP] == s[rightP] and s[leftP].isalnum() and s[rightP].isalnum():
                leftP += 1
                rightP -= 1
            elif s[leftP].isalnum() == False:
                leftP += 1
            elif s[rightP].isalnum() == False:
                rightP -= 1
            else:
                return False
        return True