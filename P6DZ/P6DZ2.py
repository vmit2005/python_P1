print("               Задача 2")
a = [int(input("Введите элемент списка " + str(i + 1) + " :")) for i in range(int(input("Введите длину списка: ")))]
print()
k = int(input("Введите индекс   : "))
c = int(input("Введите значение : "))
a.insert(k, c)
print(str(a))
