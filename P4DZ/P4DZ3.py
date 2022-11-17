a = int(input("ЧИСЛО КВАДРАТОВ"))
b = int(input("РАЗМЕР квадрата"))
for i in range(a):
    for j in range(b):
        print()
        for k in range(a):
            for l in range(b):
                print(("*" if int(i + k) % 2 == 0 else " "), end="")
