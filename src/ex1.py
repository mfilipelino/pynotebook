def solution(A, B):
    A = set(A)
    B = set(B)
    C = B - A
    if len(C) == 1:
        return C.pop()
    else:
        return -1


def test_base():
    assert 0 == solution([1, 2, 3], [0, 0, 0])
    assert 3 == solution([0, 1, 2, 4, 5], [2, 3, 3, 3, 2])
    assert -1 == solution([2, 3, 3, 4], [1, 1, 0, 0])
