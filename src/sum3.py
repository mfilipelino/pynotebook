def combination(lst, start, end, r, total, result, out_lst):

    if len(r) == total:
        if sum(r) == result:
            out_lst.append(r.copy())

    else:
        r.append(lst[start])
        combination(lst, start + 1, end, r, total, result, out_lst)
        r.pop()
        combination(lst, start + 1, end, r, total, result, out_lst)


lst = [1, 2, 3]
out_lst = []
combination(lst=lst, start=0, end=len(lst), r=[], total=3, result=0, out_lst=out_lst)

print(out_lst)