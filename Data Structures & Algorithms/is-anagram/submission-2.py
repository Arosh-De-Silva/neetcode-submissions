class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_letters:
                s_letters[s[i]] = 1
            else:
                s_letters[s[i]] += 1
            if t[i] not in t_letters:
                t_letters[t[i]] = 1
            else:
                t_letters[t[i]] += 1
        if s_letters == t_letters:
            return True
        else:
            return False