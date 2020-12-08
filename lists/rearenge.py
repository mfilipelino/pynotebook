def rearrange(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] >= 0 and lst[end] < 0:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        else:
            if lst[start] < 0:
                start += 1
            if lst[end] >= 0:
                end -= 1
    return lst


def r_rearrange(lst):
    """
    Recursive rearrange
    """
    def recursive_rearrange(lst, start, end):
        if start >= end:
            return lst
        else:
            if lst[start] >= 0 and lst[end] < 0:
                lst[start], lst[end] = lst[end], lst[start]
                return recursive_rearrange(lst, start + 1, end - 1)
            else:
                if lst[start] < 0:
                    return recursive_rearrange(lst, start + 1, end)
                if lst[end] >= 0:
                    return recursive_rearrange(lst, start, end - 1)

    return recursive_rearrange(lst, start=0, end=len(lst) - 1)


def test_base():
    assert [] == rearrange([])
    assert [1] == rearrange([1])
    assert [-1] == rearrange([-1])


def test_case1():
    assert [-1, 2] == rearrange([-1, 2])
    assert [-2, 1] == rearrange([-2, 1])


def test_case2():
    assert [-6, -1, -9, 4, 5, 20, 10] == rearrange([10,-1,20,4,5,-9,-6])
    assert [-6, -1, -9, 4, 5, 20, 10] == r_rearrange([10,-1,20,4,5,-9,-6])