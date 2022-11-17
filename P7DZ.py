import random

print("Задание 1")
a = [random.randint(0, 100) for i in range(int(input("Количество элементов: ")))]
s = int(sum(a))
print("Сгенерированный  список", a)
print("Cумма элементов списка", s)
print()
print()

print("Задание 2")
a = [random.randint(-100, 100) for i in range(int(input("Количество элементов: ")))]
print(a)

a.sort(reverse=True)
print("Отсортированный список", a)
print()
print()

print("Задание 2 вариант")
a = [random.randint(-100, 100) for i in range(int(input("Количество элементов: ")))]
print(a)
a_plus, a_minus = [], []
for i in a:
    if i > 0:
        a_plus.append(i)
    else:
        a_minus.append(i)
a_plus.sort(reverse=True)
a = a_plus + a_minus
print("Отсортированный список", a)
print()
print()

print("Задание 3")
a = [int(input("Введите элемент списка " + str(i + 1) + " :")) for i in range(int(input("Введите длину списка: ")))]
n = int(input("ВВедите число, которое нужно найти"))
print("Введенный список", a)
a.pop(a.index(n))
a.sort(reverse=True)
print("Измененный список", a)
