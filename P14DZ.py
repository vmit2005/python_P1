print('Задание1')


def fuch_compute(a):
    def inner(b):
        return a * b

    return inner


res = fuch_compute(2)
print(res(15))
print(res(20))
res = fuch_compute(3)
print(res(15))
print(res(20))
print()
print()
print("Задание 2")


def s_par(a, b, c):
    def s_rech(b, h):
        return b * h

    r = s_rech
    return 2 * r(a, b) + 2 * r(b, c) + 2 * r(a, c)


print(s_par(2, 4, 6))
print(s_par(5, 8, 2))
print(s_par(1, 6, 8))
