# rozwiazanie zadania z LEKCJI 3
# zadanie 3.5
# DAMIAN PORADYLO

length = 15
measure = "|"

for i in range(0, length):
    measure += "....|"

measure += "\n"

for i in range(0, length+1):
    if i >= 9:
        measure += str(i) + "   "
    else:
        measure += str(i) + "    "


print(measure)


