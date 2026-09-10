import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
q = [int(x) for x in input_data[1: n+1]]
current_sum  = sum(q[:k])
result = []
result.append(current_sum / k)
for i in range(k, n):
    current_sum = current_sum - q[i - k] + q[i]
    result.append(current_sum / k)
print(''.join(map(str, result)))
solve()

