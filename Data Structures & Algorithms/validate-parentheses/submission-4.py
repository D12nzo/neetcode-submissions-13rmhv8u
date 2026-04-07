class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'}
        stack = []
        for symb in s:
            if symb not in pairs:
                stack.append(symb)
            else: 
                if not stack or stack[-1] != pairs[symb]:
                    return False
                stack.pop()

        return not stack