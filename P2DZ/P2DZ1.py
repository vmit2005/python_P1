num = int(input("ВВЕДИТЕ ЦЕЛОЕ ПЯТИЗНАЧНОЕ ЧИСЛО : "))
n = num
rez1 = 1
rez2 = 0
for i in range(1, 6, 1):
    cifra = num % 10
    rez1 = rez1 * cifra
    rez2 = rez2 + cifra
    num = num // 10
    # print(cifra, rez1, rez2)
print("ПРОИЗВЕДЕНИЕ ЦИФР ЧИСЛА " + str(n) + " :" + str(rez1))
print("CРЕДНЕЕ АРИФМЕТИЧЕСКОЕ  " + str(n) + " :" + str(rez2 / 5))
