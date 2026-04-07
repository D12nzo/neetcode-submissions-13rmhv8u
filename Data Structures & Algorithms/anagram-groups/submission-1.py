class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in sets:
                sets[key] = []
            sets[key].append(word)
        
        return list(sets.values())