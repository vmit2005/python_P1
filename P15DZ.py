print('Задание 1 ')

print((lambda x, y, z: x * y * z)(2, 5, 5))
rez = (lambda x, y, z: x * y * z)
print(rez(2, 5, 5))
print()
print()


print('Задание 2 ')
der_liste = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]
print('Сортировка по имени')
der_liste.sort(key=lambda i: i['name'])
print(der_liste)
print('Сортировка по баллам')
p = sorted(der_liste, key=lambda i: i['final'], reverse=True)
print(p)
print()
print()


print('Задание 3 ')
l_min = {'name': '', 'final': 101}
l_max = {'name': '', 'final': 0}

l_mn = lambda i: (i if i['final'] < l_min['final'] else l_min)
l_mx = lambda i: (i if i['final'] > l_max['final'] else l_max)

for i in der_liste:
    l_min = l_mn(i)
    l_max = l_mx(i)

print("Минмальная оценка", l_min)
print("Максимальная оценка", l_max)
print()
print()


print("Задание 4")
print("Исходный  список")
nums = [3, 5, 7, 3, 9, 5, 7, 2]
num2 = list(map(lambda x: x * x, nums))
num3 = list(map(lambda x: x * x * x, nums))
print("Список квадратов")
print(num2)
print("Список кубов")
print(num3)
