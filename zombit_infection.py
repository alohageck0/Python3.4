__author__ = 'royalfiish'

popula = [[6, 7, 2, 7, 6],
          [6, 3, 1, 4, 7],
          [0, 2, 4, 1, 10],
          [8, 1, 1, 4, 9],
          [8, 7, 4, 9, 9]]


def answer(population, y, x, strength):
    global popula
    popula = population
    x_max_col = len(popula[0])
    y_max_row = len(popula)

    def next_round(popul, iterx):
        global popula
        popula = popul
        for i in range(iterx + 1):
            for x_row in popula:
                for y_col in range(len(x_row)):
                    if x_row[y_col] == -1:
                        neighbors = find_neighbors(popula.index(x_row), y_col)
                        for neighbor in neighbors:
                            if popula[neighbor[0]][neighbor[1]] <= strength:
                                popula[neighbor[0]][neighbor[1]] = -1

    def find_neighbors(x, y):
        coords = [[] for i in range(4)]
        coords = [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]]

        def clean_arr(arr):
            for i in arr:
                if i[0] < 0 or i[1] < 0 or i[1] > (x_max_col - 1) or i[0] > (y_max_row - 1):
                    arr.remove(i)
                    return clean_arr(arr)

        clean_arr(coords)
        return coords

    if popula[x][y] <= strength:
        popula[x][y] = -1
    else:
        return popula
    if x_max_col >= y_max_row:
        maxiter = x_max_col
    else:
        maxiter = y_max_row
    next_round(popula, maxiter)

    return popula


first = answer(popula, 4, 4, 10)
for i in range(len(first)):
    print(first[i])

'''
[[1, 2, 3], [2, 3, 4], [3, 2, 1]]

[[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
'''
