fib = [1, 1]

for i in range(15):
    fib.append(fib[-1] + fib[-2])


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


nazwiska = []
with open("naziwska.txt", 'r', encoding='UTF-8') as f:
    for line in f:
        nazwiska.append(line.strip())


def binary_search(nazwiska, delikwent, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if nazwiska[mid] == delikwent:
        return mid
    elif nazwiska[mid] < delikwent:
        return binary_search(nazwiska, delikwent, mid + 1, high)
    else:
        return binary_search(nazwiska, delikwent, low, mid - 1)


print(binary_search(nazwiska, "Strykowski", 0, len(nazwiska) - 1))
