def f(a):
    if a <= 1:
        return 0
    elif a == 2:
        return 1
    else:
        return f(a - 1) + a


def solution(A):
    result = []
    for i in range(1, len(A)):
        result.append(A[i] - A[i - 1])

    first = result.pop(0)
    count = 1
    r = 0
    for c in result:
        if c == first:
            count += 1
        else:
            r += f(count - 1)
            first = c
            count = 1

    if r > 1000000000:
        return -1
    else:
        return r


def test_base():
    print()
    print(solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))

