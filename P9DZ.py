print("Введите кортеж, по одному числу.\nДвойное нажатие ЕNTER будет означать конец кортежа")
lstt = []
while True:
    a = input("--> ")
    if a == "":
        break
    else:
        try:
            lstt.append(int(a))
        except ValueError:
            pass

t = tuple(lstt)
e = int(input("Введите искомый элемент"))


def sliser(tpl, element=1):
    print("КОРТЕЖ: ", tpl, " Искомый элемент:", element)
    try:
        a1 = tpl.index(element)
    except ValueError:
        print("Нет такого значения ни первого, ни второго")
        return ()
    try:
        a2 = tpl.index(element, a1 + 1)
        return tpl[a1:a2 + 1]
    except ValueError:
        print("Нет второго искомого значения")
        return tpl[a1:]


print("BBЕДЕНО С КЛАВИАТУРЫ")
print(sliser(t, e))
print()
print("Значения записаны в код")
print(sliser((1, 2, 3), 8))
print(sliser((1, 2, 8, 5, 1, 2, 9), 8))
print(sliser((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(sliser((8, 3, 4, 8)))
print(sliser((8, 5, 1, 2, 9)))
print(sliser(()))
