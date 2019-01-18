# rozwiazanie zadania z LEKCJI 3
# zadanie 3.9
# DAMIAN PORADYLO


sekwencja = [[], [4], (1, 2), (3, 4), (5, 6, 7, 1)]
result = []

for i in sekwencja:
    w = 0
    for z in range(0, len(i)):
        w += i[z]
    result.append(w)

print(sekwencja)
print(result)
