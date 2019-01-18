#3.5


def ruler(x):
    measure = "|"
    for i in range(0, x):
        measure += "....|"
    measure += "\n"
    for i in range(0, x+1):
        if i >= 9:
            measure += str(i) + "   "
        else:
            measure += str(i) + "    "
    return measure


#3.6


def net(x, y):
    poziomo = "---+"
    pionowo = "   |"
    main_string = ""
    for i in range(0, y + 1):
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
    return main_string


print(ruler(12))
print(net(3, 3))
