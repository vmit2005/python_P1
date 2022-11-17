import re
print("Задание1")
def pass_valid(s1=input('Enter password: ')):
    """
    Валидатор

    Ввод и проверка пароля.
    Eсли пароль неправильный возвращает ""
    :param s1: type=str
    :return: str или False
    """
    r = r'^[\da-zA-Z0-9@_-]{6,18}$'
    r2="".join(re.findall(r, s1))
    return (r2 if r2 else False)
print (pass_valid())
print()
print()
print('Задание 2')
s1='MMDCCLXXIX'
r=r'^M{,3}D?C{,3}M?L?X{,3}C{,3}I{,3}X?V?I{,3}$'
print("".join(re.findall(r,s1)))
