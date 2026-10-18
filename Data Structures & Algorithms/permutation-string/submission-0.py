class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        s2dict = {}
        for letter in s1:
            s1dict[letter] = s1dict.get(letter, 0) + 1
        l = 0
        for r in range(len(s2)):
            s2dict[s2[r]] = s2dict.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                s2dict[s2[l]] -= 1
                if s2dict[s2[l]] == 0:
                    del s2dict[s2[l]]
                l += 1
            if r - l + 1 == len(s1) and s1dict == s2dict:
                return True
        return False