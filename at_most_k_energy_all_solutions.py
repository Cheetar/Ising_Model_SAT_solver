import pycosat


# mapowanie rejestrow, krawedzi i punktow


def numer_rejestru(i, j):
    return l + (i - 1) * k + j


def numer_punktu(i, j):
    return l + 1 + (l - 1) * k - 1 + (j - 1) * n + i


def numer_krawedzi(i, j):
    return (j - 1) * n + i

# n-liczba punktow w boku siatki
# d-wymiar siatki (ale na razie brak klauzul na sasiedztwo w innych
# wymiarach, wiec d=const=2)
n = 7
d = 2

# k-licznik stanu energetycznego
# l-liczba krawedzi - polaczen miedzy sasiadami
l = 2 * n**d
k = 49  # nawet jakby sie chialo to nie mozna zero

# zakresy na iksy-krawedzie,rejestry-rejestry, punkty-punkty
iksy = range(1, l + 1)
rejestry = range(l + 1, l + 1 + (l - 1) * k)
punkty = range(l + 1 + (l - 1) * k, l + 1 + (l - 1) * k + n**d)

# pusta poczatkowo lista wszystkich klauzul
klauzule = []


# 1 pierwsza wartosc taka jak zmienna, reszta zerowych w pierwszym rejestrze
klauzule += [[-1, numer_rejestru(1, 1)], [1, -numer_rejestru(1, 1)]]
for j in range(2, k + 1):
    klauzule += [[-numer_rejestru(1, j)]]
# (1 i 2 z tablicy)


# 2 jesli ktorys pierwszy bit jest 1 to poprzedni u gory byl 1 lub xi jest 1
for i in range(2, l):
    klauzule += [[-numer_rejestru(i, 1), numer_rejestru(i - 1, 1), i], [-numer_rejestru(
        i - 1, 1), numer_rejestru(i, 1)], [-i, numer_rejestru(i, 1)]]
# (3 z tablicy)


# 3 jeden na danym miejscu gdy x1 jest 1 i powyzej na skos jest 1 lub
# powyzej bylo 1
for i in range(2, l):
    for j in range(2, k + 1):
        klauzule += [[numer_rejestru(i, j), -numer_rejestru(i - 1, j)],
                     [numer_rejestru(i - 1, j), -numer_rejestru(i, j), i]]
        klauzule += [[-numer_rejestru(i - 1, j - 1), numer_rejestru(i, j), -i], [
            numer_rejestru(i - 1, j - 1), numer_rejestru(i - 1, j), -numer_rejestru(i, j)]]
# (4 z tablicy)


# 4 jesli nastepny x jest 1 a ostatnia wartosc w poprzednim rejestrze jest
# 1 to zle
for i in range(1, l):
    klauzule += [[-numer_rejestru(i, k), -(i + 1)]]
# (5 z tablicy)


# 5 Klauzule na xnory
for j in range(1, n + 1):
    for i in range(1, n + 1):
        klauzule += [[-numer_punktu(i, j), -numer_punktu(i % n + 1, j), numer_krawedzi(i, j)], [numer_punktu(i, j), numer_punktu(i % n + 1, j), numer_krawedzi(
            i, j)], [numer_punktu(i, j), -numer_punktu(i % n + 1, j), -numer_krawedzi(i, j)], [-numer_punktu(i, j), numer_punktu(i % n + 1, j), -numer_krawedzi(i, j)]]

for j in range(1, n + 1):
    for i in range(1, n + 1):
        klauzule += [[-numer_punktu(i, j), -numer_punktu(i, j % n + 1), numer_krawedzi(i, j) + n**d], [numer_punktu(i, j), numer_punktu(i, j % n + 1), numer_krawedzi(i, j) + n**d], [
            numer_punktu(i, j), -numer_punktu(i, j % n + 1), -(numer_krawedzi(i, j) + n**d)], [-numer_punktu(i, j), numer_punktu(i, j % n + 1), -(numer_krawedzi(i, j) + n**d)]]


# wypisywanie:

# for i in list(pycosat.itersolve(klauzule)):
#    print i

# liczba rozwiazan:

# print len(list(pycosat.itersolve(klauzule)))


def klauzle_to_txt(klauzule, path):
    with open(path, "w") as out:
        for klauzula in klauzule:
            for num in klauzula:
                out.write(str(num) + " ")
            out.write("0\n")

klauzle_to_txt(klauzule, "input.txt")
