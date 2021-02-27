def solution(lst):
    lst = list(bin(lst))
    indices = dict()
    count_0 = -1
    for i in range(2, len(lst)):
        if lst[i] == 0 and count_0 == False:
            indices[i] = 0
        elif lst[i] == 0 and count_0 == True:
            indices[i] += 1
        elif lst[i] == 1 and count_0 == True:
            pass

