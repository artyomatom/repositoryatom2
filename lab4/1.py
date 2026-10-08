import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    street = input_data[1:]
    ans = [0] * n
    
    last_zero = -1
    for i in range(n):
        if street[i] == '0':
            last_zero = i
            ans[i] = 0
        else:
            if last_zero != -1:
                ans[i] = i - last_zero
            else:
                ans[i] = n
    last_zero = -1
    for i in range(n - 1, -1, -1):
        if street[i] == '0':
            last_zero = i
        else:
            if last_zero != -1:
                dist = last_zero - i
                if dist < ans[i]:
                    ans[i] = dist
                
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()