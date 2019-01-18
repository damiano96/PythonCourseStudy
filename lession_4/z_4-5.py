def odwracanie_iteracyjne(L, left, right):
    L[left:right+1] = L[left:right+1][::-1]


def odwracanie_rekurencyjne(L, left, right):
    if right <= left:
        return
    else:
        L[left], L[right] = L[right], L[left]
        return odwracanie_rekurencyjne(L, left+1, right-1)


L = [2, 3, 6, 4, 1, 5]
odwracanie_iteracyjne(L, 1, 4)
print(L)

L = [2, 3, 6, 4, 1, 5]
odwracanie_rekurencyjne(L, 1, 4)
print(L)
