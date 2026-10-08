import sys

def solve():
    s = sys.stdin.read().lower()
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if left < right:
            if s[left] != s[right]:
                print("False")
                return
            left += 1
            right -= 1
    
    print("True")

if __name__ == '__main__':
    solve()