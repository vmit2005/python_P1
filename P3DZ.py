a = None
while a is None:
    try:
        a = int(float(input("Введите начало диапазона: ")))
    except ValueError:
        a = None

b = None
while b is None:
    try:
        b = int(float(input("Введите конец диапазона: ")))
    except ValueError:
        b = None


#
# if a > b:
#     a, b = b, a
a, b = ((a, b) if a < b else (b, a))
rez, a1 = 0, a
while a1 <= b:
    if a1 % 2 != 0:
        rez = rez + a1

    a1 += 1
print("Сумма всех целых нечетных чисел, от " + str(a) + " до " + str(b) + " равна " + str(rez))
