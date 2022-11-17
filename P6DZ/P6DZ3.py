print("               Задача 2")
a = [int(input("Введите элемент списка " + str(i + 1) + " :")) for i in range(int(input("Введите длину списка: ")))]
print()
ch = int(input("Введите число   : "))
for i in a:
    if ch == i:
        print("Число присутствует в элементах списка")
        break
else:
    print("В списке такого числа нет")
