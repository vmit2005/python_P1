print("Задание 1")
s = "Дана ст(рока символов, среди кторых есть одна открыв)ающаяся"
print(s)
print(s[s.find("(") + 1:s.rfind(")")])
print(s[s.index("(") + 1:s.rindex(")")])
print(s.strip('(Данстющяс )'))
print(s.lstrip('Данст (').rstrip(')ающяс'))
print()
print()
print("Задание 2")
s = input("Исходная строка")
# s='11 23 44 55 23 22'
s1 = input("Подстрока")
# s1="23"
s2 = input("Подстрока на замену")
# s2='!!!'
while True:
    if s.find(s1) != -1:
        s = s[:s.find(s1)] + s2 + s[s.find(s1) + len(s1):]
    else:
        break
print(s)
print()
print()
print("Задание 3")


def tipa_split(strrr):
    s, s1 = [], ""
    for i in strrr:
        if i != " ":
            s1 = s1 + i
        else:
            s.append(s1)
            s1 = ""
    return s

    # s=input("Введите строку рускоязычного текста").split() этот оператор еще не проходили


s = tipa_split(input("Введите строку рускоязычного текста"))
rez = 0
for i in s:
    if i[0] == 'е' or i[0] == 'Е':
        rez += 1
print("Число слов начинающихся с е: ", rez)
