def sum_seq(sequence):
    wynik = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            wynik += sum_seq(i)
        else:
            wynik += i
    return wynik


sequence = [[1, 2], [2, 4, 6, 8], [3], [[3, [1, [1, 3], 4], 6]]]

print(sum_seq(sequence))

