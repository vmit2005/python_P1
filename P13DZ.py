print("Задание 1")


def composition(*args):
    rez = 1
    for i in args:
        rez *= i
    return rez


print(composition(9, 10))
print(composition(2, 3, 4))
print(composition(3, 5, 10, 6))
print()
print()
print("Задание 2")


def summ(*args):
    rez, rez_str = 0, ""
    for i in args:
        rez += i
        rez_str += str(rez) + " "  # Знаю можно проще. Захотелось, чтобы вывод был через ретурн.

    return rez_str


print(summ(3, 9, 1))
print(summ(2, 5, 4, 2))
print(summ(3, 5, 10, 6, 3))
print()
print()
print('Задание 3')


def figa(figure_type=False, **kwargs):
    def romb(d1, d2):
        return d1 * d2 / 2

    def squa(a):
        return a * a

    def trap(a, b, h):
        return (a + b) * h * 0.5

    def circ(r):
        return 3.14159 * r * r

    if figure_type == 'rhombus':
        return (romb(d1=kwargs['d1'], d2=kwargs['d2']))
    elif figure_type == 'square':
        return (squa(a=kwargs['a']))
    elif figure_type == 'circle':
        return (circ(r=kwargs['r']))
    elif figure_type == 'trapezoid':
        return (trap(a=kwargs['a'], b=kwargs['b'], h=kwargs['h']))
    else:
        return 'invalid data'


print(figa('rhombus', d1=10, d2=8))
print(figa('square', a=5))
print(figa('trapezoid', b=3, a=12, h=6)) # изменена последовательность a,b,h
print(figa('circle', r=18))
print(figa('unknown', a=12, b=3, h=6))
