print("Задание 1")
l = [-2, 3, 8, -11, -4, 6]


def sum_minus(s):
    if len(s)==0:
        return 0
    return sum_minus(s[1: ])+(1 if s[0] < 0 else 0)


print('n =',sum_minus(l))


print("Задание 2")
names = ['Adam', ["Bob", ["Chet", "Cat", ["Lena", ["Andrey", "Pit"]]], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'An']


def list_to_list(nam):
    """
    CПРЯМЛЯТОР

    Спрямляет список на один уровень вложенности
    :param nam: list
    :return: list
    """
    nam1 = []
    for i in nam:
        # print(type(i))
        if type(i) == str:
            nam1.append(i)
        if type(i) == list:
            for j in i:
                # print(j)
                nam1.append(j)
    return nam1


def nam_type(nam):
    """
    ИНДИКАТОР ВЛОЖЕННОСТИ

    определяет наличие вложенных  списков
    :param nam: list
    :return: True - если   влеженные списки есть
             False- вложенных списков нет
    """
    t = False
    for i in nam:
        if type(i) == list:
            t = True
    return t


t = True
while t:
    names = list_to_list(names)
    # print(names)
    t = nam_type(names)

print("Число элементов списка, со всеми вложенными", len(names))
