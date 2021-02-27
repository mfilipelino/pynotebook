def solution(N):
    result = []
    s = str(N)
    s_len = len(s) + 1
    i = 0
    first = True

    if s[0] == '-':
        result.append('-')
        i += 1
        while len(result) < s_len:
            if int(s[i]) > 5 and first:
                result.append('5')
                first = False
            else:
                result.append(s[i])
                i += 1
    else:
        while len(result) < s_len:
            if int(s[i]) < 5 and first:
                result.append('5')
                first = False
            else:
                result.append(s[i])
                i += 1

    return int(''.join(result))


def test_base():

    print(solution(268))
    print(solution(670))
    print(solution(0))
    print(solution(-999))
    print(solution(-499))

