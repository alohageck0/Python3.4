def answer(x):
    def sum_remain(n):
        summa = 0
        for x in range(0, n):
            summa += 3 ** x
        return summa

    left = x
    right = 0
    index_arr = [i for i in range(100)]
    index_dict = dict()
    max_ind = int
    for i in index_arr:
        summ = right
        right += 3 ** i
        if (left + summ) >= 3 ** i:
            max_ind = i
    max_ind_arr = [x for x in range(max_ind)]
    right = 3 ** max_ind
    index_dict[max_ind] = 'R'
    for _ in reversed(max_ind_arr):
        remain___ = left + sum_remain(_)
        if left == right:
            index_dict[_] = "-"
            continue
        elif remain___ < right:
            left += 3 ** _
            index_dict[_] = "L"
            continue
        elif remain___ > right:
            if remain___ < right + 3 ** _:
                index_dict[_] = "-"
                continue
            right += 3 ** _
            index_dict[_] = 'R'
            continue
        elif (left + 3 ** _) > (right + sum_remain(_)):
            index_dict[_] = "-"
            continue
    return list(index_dict.values())
