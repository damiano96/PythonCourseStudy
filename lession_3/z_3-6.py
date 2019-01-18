# rozwiazanie zadania z LEKCJI 3
# zadanie 3.6
# DAMIAN PORADYLO

x = 5
y = 5

poziomo = "---+"
pionowo = "   |"
main_string = ""
for i in range(0, y+1):
    string1 = "+"
    string2 = "|"
    for w in range(0, x):
        string1 += poziomo
        string2 += pionowo
    string1 += "\n"
    string2 += "\n"
    main_string += string1
    if i < y:
        main_string += string2

print(main_string)

