import sys

def is_correct_bracket_seq(s: str) -> bool:
    stack = []
    
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set('({[')
    
    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    
    return len(stack) == 0

def solve():
    s = sys.stdin.readline().strip()
    print("True" if is_correct_bracket_seq(s) else "False")

if __name__ == '__main__':
    solve()