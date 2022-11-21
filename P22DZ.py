import re

def num_tel(num1):
     """
     Валидатор

     Проверяет соответствие номера телефона заданию.
     Не меняет Формат телефона.
     """
     reg=r'[+7|7][\s]*[(]*[\s]*\d{3}[\s]*[)]*[\s]*\d{3}[\s]*-*[\s]*\d{2}[\s]*-*[\s]*\d{2}'
     num=re.findall(reg,num1)
     return num
print('Вариант 1')
print(num_tel("+7 499 456-45-78"))
print(num_tel("+74994564578"))
print(num_tel("7 (499) 456 45 78"))
print(num_tel("7 (499) 456-45-78"))
print(num_tel('+7 499 4562345'))
print()
print()
print("Вариант 2")



def num_tel2(num1):
    """
    Стандартизатор
    приводит номера телефонов к единому формату.

    """
    n="".join(re.findall(r'\b[+\d]*\b',num1))
    return ("+7"+n[1:] if n[0]=="8" else n if n[0]=='+' else "+"+n)

print(num_tel2("+7 499 456-45-78"))
print(num_tel2("+74994564578"))
print(num_tel2("7 (499) 456 45 78"))
print(num_tel2("7 (499) 456-45-78"))
print(num_tel2('7 499 4562345'))
print(num_tel2('8 499 4562345'))