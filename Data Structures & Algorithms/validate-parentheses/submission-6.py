

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in par_map:
                if stack and par_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack