def fibonacci(n):
    result = [0, 1]
    for i in range(0, n):
        result.append(result[i] + result[i+1])
    return result[n]


print(fibonacci(15))
