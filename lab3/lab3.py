def two_sum_wsort(numbers, k):

    numbers.sort()

    left = 0
    right = len(numbers) - 1 # ошибка была в том, что я неправильно задал переменную

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == k:
            return numbers[left], numbers[right]
        if current_sum < k:
            left += 1
        else:
            right -=1
    return None

n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

result = two_sum_wsort(numbers, k)
if result:
    print(result[0], result[1])
else:
    print()

