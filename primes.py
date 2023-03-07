from math import sqrt


def is_prime(n):
    if 1 >= n:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sito(n):
    numbers = [True for _ in range(n)]
    primers = []
    for i in range(len(numbers)):
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i]:
                primers.append(i)
                for j in range(i,len(numbers), i):
                    numbers[j] = False

    return primers
