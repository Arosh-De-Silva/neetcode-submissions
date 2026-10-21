class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matchingDicts = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in matchingDicts:
                matchingDicts[key].append(word)
            else:
                matchingDicts[key] = [word]
        answer = []
        for key, value in matchingDicts.items():
            answer.append(value)
        return answer