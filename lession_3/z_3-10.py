# rozwiazanie zadania z LEKCJI 3
# zadanie 3.10
# DAMIAN PORADYLO


roman = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
roman2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman2int(romanNumber):
    i = 0
    result = 0
    subtract = 0
    while i < len(romanNumber):
        if i < len(romanNumber)-1:
            if roman.get(romanNumber[i]) < roman.get(romanNumber[i+1]):
                result += (roman.get(romanNumber[i+1]) - roman.get(romanNumber[i]))
                i += 2
                continue
        result += roman.get(romanNumber[i])
        i += 1

    result -= subtract
    return result


print(roman2int("MMXVIII")) #2018
print(roman2int("MMMDCCCLXXXVIII")) #3888
print(roman2int("MCMLVI")) #1956
