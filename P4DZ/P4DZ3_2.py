a = int(input("ЧИСЛО КВАДРАТОВ"))
b = int(input("РАЗМЕР квадрата"))
for i in range(a * b):
    print()
    for j in range(a * b):
        k = i // a
        l = j // a
        print(("*" if int(l + k) % 2 == 0 else " "), end="")
