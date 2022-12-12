def file_sum(a, b, c="sum.file"):
    f = open(c, "wb")
    f1 = open(a, "rb")
    d = f1.read()
    f.write(d)
    f1 = open(b, "rb")
    d = f1.read()
    f.write(d)
    f1.close()
    f.close()


w = True
while w:
    try:
        print("Введите обозначение первого файла или нажмите [ENTER]")
        af = input("По умолчанию будет выбран файл P26DZ1.txt")
        if af == "":
            af = "P26DZ1.txt"
        print("Введите обозначение второго файла или нажмите [ENTER]")
        bf = input("По умолчанию будет выбран файл P26DZ2.txt")
        if bf == "":
            bf = "P26DZ2.txt"
        file_sum(af, bf, "P26DZ3.txt")
        print(f"Файлы {af} и {bf} скрпированы в файл  P26DZ3.txt")
        w = False
    except FileNotFoundError:
        print()
        print("Указанные файлы не найдены")
        print()
        w = True
# print(af,bf)
