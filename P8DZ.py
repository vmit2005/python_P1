from random import randint


def new_matrix(row, col, rnd_min=0, rnd_max=0):
    '''Новая матрица
    Число строк, число знаков в строке,
    минимальное и максимальное значение для рандоминт
    если задано два параметра матрица заполняется 0'''
    if rnd_min == 0 and rnd_max == 0:
        return ([[0 for i in range(col)] for j in range(row)])
    else:
        return ([[randint(rnd_min, rnd_max) for i in range(col)] for j in range(row)])


def new_matrix_123(row, col):
    c, mm = 1, []
    for j in range(row):
        d = []
        for i in range(col):
            d.append(c)
            c += 1
        mm.append(d)
    return (mm)


def transpoz(matrix):
    '''Транспозиция матрицы.
    Принимает матрицу. Матрицу возвращает.
    '''
    a, b = len(matrix), len(matrix[0])
    matrix2 = new_matrix(b, a)
    for i in range(a):
        for j in range(b):
            matrix2[j][i] = matrix[i][j]
    return matrix2


def prnt_matrix(matr):
    '''Печать матрицы'''
    for i in matr:
        for j in i:
            print(j, end="\t\t")
        print()


print("Задание 1")
print('Исходная матрица')
# m = new_matrix(6, 4, -100, 100)
m = new_matrix_123(3, 4)
prnt_matrix(m)
print()
print('Матрица после транспозициии')
m1 = transpoz(m)
prnt_matrix(m1)
print()
print()

print("Задание 2")
m = new_matrix(6, 6, 0, 10)
line = [randint(0, 10) for i in range(6)]
print("Матрица")
prnt_matrix(m)
print("Одномерный список", line)
for i in range(1, len(m), 2):
    m[i] = line

print("Maтрица после замены")
prnt_matrix(m)
