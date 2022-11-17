num = int(input("ВВедите число от 1 до 99 :"))
if 0 < num < 100:
    if (num == 1 or num > 20) and num % 10 == 1:
        print(str(num) + " копейка")
    elif (num == 1 or num > 20) and 1 < num % 10 < 5:
        print(str(num) + " копейки")
    else:
        print(str(num) + " копеек")
else:
    print("Введенное число не входит в диапазон 1...99")
