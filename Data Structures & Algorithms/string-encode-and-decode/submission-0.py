class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result
    
    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            delimiter_pos = s.index('#', i)
            length = int(s[i:delimiter_pos])
            start = delimiter_pos + 1
            result.append(s[start:start + length])
            i = start + length
        
        return result