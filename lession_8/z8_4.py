import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    if a+b > c and a+c > b and b+c > a:
        p = (a+b+c)/2.0
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        raise ValueError("Z tych bokow nie mozna stworzyc trojkata")

try:
    heron(2, 3, 7)
except ValueError:
    print("Wystapil wyjatek")

print(heron(3, 4, 5))
print(heron(3.5, 4, 5))

