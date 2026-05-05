class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        act = { '+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: int(x / y) 
               }  
        mas = []
        for char in tokens:
            if char not in act.keys():
                mas.append(int(char))
            else:
                y = mas.pop()
                x = mas.pop()
                mas.append(act[char](x,y))
        return mas[0]