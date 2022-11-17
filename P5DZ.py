print("ВВедите элементы списка")
a = [int(input("->")) for i in range(int(input("Количество элементов: ")))]
for i in range(1, len(a), 1):
    if a[i] > a[i - 1]:
        print(a[i], "     (" + str(a[i]) + " > " + str(a[i - 1]) + " )")
