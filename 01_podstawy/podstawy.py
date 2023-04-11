# stan_konta = input("Podaj stan konta ")
# stan_konta = int(stan_konta)
# stan_konta = stan_konta + 500*2

# print(stan_konta)
from copy import deepcopy

x = 8
y = x // 2
x = x ** (1 / 2)
"""print(x)

temperature = 15
czy_szczesliwy = False
if not temperature <= 10 or czy_szczesliwy:
    print("wychodzimy")
elif temperature > -10 and czy_szczesliwy:
    print("ubierz sie ciepło")
else:
    print("nie wychodzimy")

for i in range(1, 10, 2):
    if i == 5:
        break

    print(i)"""

'''while temperature > 10:
    print('temperatura jest ok', temperature)
    temperature -= 1'''

oceny = [4, 5, 3, 2, 1, 6, 4]

"""for i in range(len(oceny)):
    print(oceny[i], end=" ")


for ocena in oceny:
    print(ocena, end=" ")
print()"""

for i, ocena in enumerate(oceny):
    if i % 2 == 0 and ocena > 3:
        print(i, ocena)
"""
for i, ocena in enumerate(oceny):
    oceny[i] += 1"""

"""oceny.append(5)
oceny.extend([3, 1, 2])
oceny.insert(4, 4)
oceny.pop()
oceny = sorted(oceny, reverse=True)

if 4 in oceny:
    print("jest taka ocena")

oceny_all = [[1, 2, 3, 5, 2, 3], [6, 6, 6], [3, 3, 4]]

for student in oceny_all:
    for ocena in student:
        print(ocena, end=' ')
    print()

oceny_2 = deepcopy(oceny_all)
oceny_2[0][0] = 123
print(oceny_all)

oceny = [4, 5, 3, 2, 1, 6, 3, 6, 5, 4]
oceny_marka = [1, 2, 3, 2, 1, 2, 1]
oceny_kozaka = [6, 5, 4, 3, 6, 6, 6, 6]

marek_set = set(oceny_marka)
kozak_set = set(oceny_kozaka)
print(kozak_set.difference(marek_set))

oceny = list(set(oceny))
print(oceny)

oceny_all = [[1, 2, 3, 5, 2, 3], [6, 6, 6], [3, 3, 4]]

oceny_slownik = {}
oceny_slownik["marek"] = [1, 2, 3, 5, 2, 3]
oceny_slownik['kozak'] = [6, 6, 6]
print(oceny_slownik['marek'])

for imie, oceny in oceny_slownik.items():
    print(imie, oceny)

for oceny in oceny_slownik.values():
    print(oceny)


"""

name = 'Wojtek'

print(name)
if 'w' in name:
    print("jest taka literka")

print(len(name))
name = name.replace("jte", "chuj")
test_string = "ala ma kota i jd"

if test_string.startswith('ALA'):
    print("jd")

new_string = name + test_string
new_string = f"{name} jest super kozakiem, a {test_string}"
print(new_string)

print(new_string[-2])

print(new_string[3:-3])

lines = []

with open("plik.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(int(line.strip()))
    print(lines)


def silnia(n):
    # 5! = 1 * 2 * 3 * 4 *5
    res = 1
    for x in range(1, n + 1):
        res = res * x
    return res


for number in lines:
    print(silnia(number))

from math import gcd, sqrt, ceil, floor

#24, 36
print(gcd(24,36))

oceny = [4, 5, 3, 2, 1, 6, 3, 6, 5, 4]

print(max(oceny))
print(min(oceny))

print(sqrt(35))
print(round(10.15152, 3))
print(ceil(10.5))
print(floor(10.5))

print(abs(-124))