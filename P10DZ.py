print("Задание 1")


def s_input():  # ВАРИАНТ
    l = []
    for i in set(input("Запишите через запятую в строку целые числа.").split(",")):
        l.append(int(i))

    l.sort()
    return tuple(l)


def s_input2():
    l = []
    b, d = 0, 1
    c = list(input("Запишите через запятую в строку целые числа."))
    print(c)
    for i in c:
        if i == '-':
            d *= -1
            continue
        try:
            b = b * 10 + int(i)
        except ValueError:
            l.append(b * d)
            b, d = 0, 1
    l.append(b*d)
    l.sort()
    l = set(l)
    print(l)
    return tuple(l)


def l13_max(sett: set):
    smax = False
    for i in sett:
        smax = (i if i > smax and i % 13 == 0 and i > 0 else smax)
    if smax == False:
        smax = "NO NUMS"
    return (smax)


print(l13_max(s_input2()))
print()
print()
print('Задание 2')
print()
s = input("Введите искомый элемент")

t = ('ab', 'abcd', 'cde', 'def')
print("Исходный кортеж", t)
if s in t:
    print("Yes")
else:
    print("No")
print()
print()

print("Задание 3")
print()

str = input('Введите по порядку, без пробелов,элементы кортежа')


def str_to_spis(strr):
    a = list(strr)

    a1, a2 = [], []  # Знак и количество
    for i in a:
        if i in a1:

            for j in range(len(a1)):
                if a1[j] == i:
                    a2[j] += 1


        else:
            a1.append(i)
            a2.append(1)
    return (a1, a2)


def print_spis(bb):
    bb1, bb2 = bb
    print("Статистика частотности символов")
    for i in range(len(bb1)):
        print("Количество ", bb1[i], " = ", bb2[i])


print_spis(str_to_spis(str))
