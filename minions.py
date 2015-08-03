__author__ = 'royalfiish'


def answer(x):
    global emp
    global level_up
    emp = 1
    level_up = 1
    for i in range(1, x + 1):
        level_emp = level_up * 7
        emp += level_emp
        level_up = level_emp
    return emp


print(answer(4))
