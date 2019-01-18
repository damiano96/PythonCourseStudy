def flatten(sequence):
    result = []
    for element in sequence:
        if not isinstance(element, (list, tuple)):
            result.append(element)
        else:
            result += flatten(element)
    return result


sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(flatten(sequence))
