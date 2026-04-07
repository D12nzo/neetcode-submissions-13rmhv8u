class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'}
        stack = []
        for symb in s:
            if not stack:
                stack.append(symb)
            else:
                if symb not in pairs:
                    stack.append(symb)
                elif stack[-1] == pairs[symb]:
                    stack.pop()
                else:
                    stack.append(symb)

        if not stack:
            return True       
        else:
            return False