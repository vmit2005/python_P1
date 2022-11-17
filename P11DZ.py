d = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
     }


def print_sale(dd):
    for i in dd:
        print(i)
        for j in dd[i]:
            print(j, ' : ', dd[i][j])
    print()
    print()


def add_sale(dd: dict):
    name = input("Введите имя")
    ddd = {'N': int(input("N -->")), 'S': int(input("S -->")), 'E': int(input("E -->")), 'W': int(input("W -->"))}
    dd.update({name: ddd})


def edit_sale(dd: dict):
    print("Имена пользователей")
    for i in dd:
        print(i)
    name = input("Введите имя")
    for j in dd[name]:
        print(j, dd[name][j])
    region = input('Выберите регион N/S/E/W')
    thislo = int(input('Введите число'))
    dd[name][region] = thislo


def del_sale(dd: dict):
    print("Имена пользователей")
    for i in dd:
        print(i)
    name = input("Введите имя")
    dd.pop(name)


while True:
    print_sale(d)
    print('Что нужно сделать?')
    comm = input('A(добавить)/Е(редактировать запись)/D(удалить запись)/(EXIT(выход)')
    if comm == 'A':
        add_sale(d)
    if comm == 'E':
        edit_sale(d)
    if comm == 'D':
        del_sale(d)
    if comm == 'EXIT':
        break
