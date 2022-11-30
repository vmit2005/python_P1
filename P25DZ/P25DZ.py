print('Задание 1')


def input_index():
    print('Ведите индексы строк (начиная от 0) которые нужно поменять местами')
    a = int(input("Первый индекс"))
    b = int(input("Второй индекс"))
    return (a, b)


try:
    f = open('DZ.txt', mode='r')
except FileNotFoundError:
    f = open('DZ.txt', mode="w")
    f.writelines(['Строка 1\n', 'Строка 2\n', 'Строка 3\n'])
    f.close()
    f = open("DZ.txt", mode="r")
    # Вариант1
s = f.readlines()
f.close()

while True:
    a, b = input_index()
    if 0 <= a <= len(s) - 1 and 0 <= b <= len(s) - 1:
        break
    print("Введены неправильные индексы")
s[a], s[b] = s[b], s[a]
print(s)
f = open('DZ.txt', mode="w")
f.writelines(s)
f.close()
#
# Вариант 2
f = open('DZ.txt', mode="r+")
s = f.readlines()
s[a], s[b] = s[b], s[a]
print(s)
f.seek(0)
f.writelines([])
f.writelines(s)
f.close()
print()
print()
print('Задание 2')


def inp_in():
    print('Введите индекс строки для замены')
    a = int(input('->'))
    return a



f = open("DZ.txt", mode="r")
ss = f.readlines()
f.close()
print(ss)
while True:
    a = inp_in()
    if 0 <= a <= len(s) - 1:
        break
    print("Неправильное значение")
print('ВВедите строку для замены')
s[a] = input("=>")
print(s)
f=open("DZ.txt",'r+')
f.writelines([])
f.writelines(s)
f.close()
