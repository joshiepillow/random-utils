from itertools import permutations 

def all(list):
    if (len(list) == 0):
        return [[]]

    rest = all(list[1:])
    out = []
    for i in range(list[0]):
        for r in rest:
            out.append([i] + r)
    return out

def calc(k):
    input = []
    iter = 4 * k - 1
    while (iter > 0):
        input.append(iter)
        iter -= 2
    perms = all(input)

    count = 0
    for perm in perms:
        good = True
        values = list(range(4 * k))
        for i in perm:
            a = values.pop(0)
            b = values.pop(i)
            if (a // 4 == b // 4):
                good = False
        if (good):
            count += 1
    return count

while True:
    print(calc(eval(input())))