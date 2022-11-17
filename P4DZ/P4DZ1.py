a = int(input("Начало диапазона "))
b = int(input("Конец диапазона "))
print("Нечетные числа в диапазоне " + str(a) + " ... " + str(b)+" :")
for i in range(a, b + 1, 1):
    if i % 2 != 0:
        print(((str(i) + ", ") if i != b else str(i)), end="")
