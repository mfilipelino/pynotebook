def combination(n, start, end, r):

    if start == end:
        return print(r)
    else:
        r.append(n[start])
        combination(n, start + 1, end, r)
        r.pop()
        combination(n,  start + 1, end, r)


def test_base():
    print()
    n = ['A', 'B', 'C']
    combination(n, 0, len(n), [])


