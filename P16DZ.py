def wraper(fn):
    def wrap(*args):
        quantity = len(args)
        sum = fn(*args)
        average = sum / quantity
        str_args = ""
        for i in args:
            str_args += (str(i) + ", ")
        str_args = str_args[:-2]
        return (sum, quantity, average, str_args)

    return wrap


@wraper
def summ(*args):
    return sum(args)


def print_rez(rez):
    print("Сумма  чисел ", rez[3], "= ", rez[0])
    print("Среднее арифметическое чисел", rez[3], "= ", round(rez[2], 2))
    print()


print_rez(summ(2, 3, 3, 4, 5, 6, 8))
print_rez(summ(2, 3, 3, 4, ))
print_rez(summ(2, 3, 4, 5, 6, 7, 8, 9))
print()
print()
