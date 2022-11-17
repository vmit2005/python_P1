print('Задание 1')
sa, sb, sc = {1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}
print("Исходные три словаря")
print(sa, sb, sc)
s = sa.copy()
s.update(sb)
s.update(sc)
print('Cумма словарей')
print(s)
print()
print()
print('Задание 2')
s = {'emp1': {'name': 'Jhon', 'salaru': 7500}, 'emp2': {'name': 'Emma', 'salaru': 8000},
     'emp3': {'name': 'Brad', 'salaru': 6500}}
nn = 'Brad'
new_salaru = 8500
print('Первоначальный словарь')
print(s)
for i in s:
    if s[i].get('name') == nn:
        s[i]['salaru'] = new_salaru
print('Cловарь после изменения ')
print(s)
print()
print()
print('Задание 3')
s = {}
sum,num=0,0
while True:
    name = input('Введите фамилию  имя студента. Для окончания ввода наберите EXIT: ')
    if name.upper() == 'EXIT':
        break
    ball = int(input('Введите балл'))
    sa = {name: ball}
    s.update(sa)
    sum += ball
    num += 1
print(s)
sred=float(sum/num)
print('Cредний бал: ', round(sred,2))
print()
print('Cписок студентов лучше среднего')
s_sred={}
for i in s:
    if s[i]>=sred:
        print(i, s[i])
        s_sred.update({i:s[i]})


