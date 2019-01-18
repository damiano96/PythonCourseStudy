# rozwiazanie zadania z LEKCJI 3
# zadanie 3.4
# DAMIAN PORADYLO

while True:
    x = input()
    if x == "stop":
        break
    if x.isnumeric():
        x = int(x)
        print(x, x ** 3)
    else:
        print("ERROR! Only numbers.")
        continue
