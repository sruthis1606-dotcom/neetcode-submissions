class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if len(stack)==0:

                    return False
                if pairs[stack[-1]]==ch:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False