def max_min(lst):
    return r_max_min(lst, size=len(lst))


def r_max_min(lst, size):
    # case 1
    if size <= 1:
        return lst

    # case 2
    if size == 2:
        if lst[0] < lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        return lst

    # case 3
    else:
        max_ind = 0
        min_ind = 0
        for i in range(size):
            if lst[i] > lst[max_ind]:
                max_ind = i
            if lst[i] < lst[min_ind]:
                min_ind = i

        max_value = lst.pop(max_ind)
        min_value = lst.pop(min_ind)

        tmp = r_max_min(lst, size=size - 2)
        tmp.insert(0, min_value)
        tmp.insert(0, max_value)
        return tmp


def test_base():
    assert [] == max_min([])
    assert [1] == max_min([1])


def test_case1():
    assert max_min([1, 2]) == [2, 1]
    assert max_min([2, 1]) == [2, 1]


def test_case2():
    assert max_min([1, 2, 3]) == [3, 1, 2]
    assert max_min([1, 2, 3, 4]) == [4, 1, 3, 2]
