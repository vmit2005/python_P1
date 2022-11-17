print("               Задача 1")
a = [int(input("Введите элемент списка "+str(i+1)+" :")) for i in range(int(input("Введите длину списка: ")))]
print()
s = []
max = 0
for i in a:
    if i > 0:
        s.append(i)
    max = (max if max > i else i)
print("Исходный список . . . . . . . . . . . "+str(a))
print("Cписок из положительных элементов . . "+str(s))
print("Наибольший элемент списка . . . . . . "+str(max))