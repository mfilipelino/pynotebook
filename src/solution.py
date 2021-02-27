def solution(lst):
    size = len(lst)
    numbers = dict()
    for element in lst:
        if element > 0:
            numbers[element]=None
    for i in range(1, size + 2):
        if (i in numbers) is False:
            return i


print(solution([-1, -2, -3]))
print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))