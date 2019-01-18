# rozwiazanie zadania z LEKCJI 3
# zadanie 3.8
# DAMIAN PORADYLO

sequence_1 = [2, 5, 8, 4, 1, 9, 11, 1]
sequence_2 = [1, 8, 11, 2, 1]

sequenceHelp = []

for i in range(0, len(sequence_2)):
    if sequence_2[i] in sequence_1:
        if sequence_2[i] not in sequenceHelp:
            sequenceHelp.append(sequence_2[i])
print(sequenceHelp)

sequenceHelp.clear()

listaHelp = sequence_1 + sequence_2
sequenceHelp2 = []
for i in listaHelp:
    if i not in sequenceHelp2:
        sequenceHelp2.append(i)
print(sequenceHelp2)
