# rozwiazanie zadania z LEKCJI 2
# DAMIAN PORADYLO
# Python3

#zadanie 2.10
print("ZADANIE 2.10")
line = "lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque finibus lectus non nunc dignissim vel efficitur nunc varius"
print(len(line.split()))


#zadanie 2.11
print("\n ZADANIE 2.11")
word = "brzeczyszczykiewicz"
x = list(word)
newWord = ""
z = 0
for i in x:
    z += 1
    newWord += i
    if z < len(x):
        newWord += "_"

print(newWord)


#zadanie 2.12
print("\n ZADANIE 2.12")
x = line.split()
z = 0
newWord1 = ""
newWord2 = ""
while z < len(x):
    a = list(x[z])
    newWord1 += a[0]
    newWord2 += a[len(a)-1]
    z += 1

print(newWord1)
print(newWord2)


#zadanie 2.13
print("\n ZADANIE 2.13")
x = line.split()
z = list()
for word in x:
    z.append(len(word))

print(sum(z))

#zadanie 2.14
print("\n ZADANIE 2.14")

x = line.split()
y = sorted(x, reverse=True, key=len)
print("The lognest word is: "+y[0])
print("It's have " + str(len(y[0])) + " characters")


#zadanie 2.15
print("\n ZADANIE 2.15")

L = [3, 5, 2, 1, 10, 33, 12, 11, 43, 8]
word = ""
for i in L:
    word += str(i)

print(word)


#zadanie 2.16
print("\n ZADANIE 2.16")
line = "W 2002 na konferencji w Brukseli GvR otrzymał od Free Software Foundation nagrodę FSF Award for the Advancement of Free Software za 2001 rok."
print(line.replace("GvR", "Guido van Rossum"))


#zadanie 2.17
print("\n ZADANIE 2.17")
x = line.split()
print(sorted(x))
print(sorted(x, key=len))


#zadanie 2.18
print("\n ZADANIE 2.18")
x = 10203002345030
y = str(x)
i = 0

for a in y:
    if a == "0":
        i += 1

print(i)


#zadanie 2.19
print("\n ZADANIE 2.19")
L = [33, 3, 1, 100, 333, 5, 32, 340, 10, 12, 2, 4]
word = ""
for a in L:
    word += str(a).zfill(3) + ","

print(word)
