import re
print('Задание 1')
dat=[]
while dat==[]:
    d=input("Введите дату в формате dd-mm-yyyy: ")
    #d='32-12-2005'
    reg=r'^((0\d|1\d|2\d|3[0-1])-(0\d|1[0-2])-(19|20)\d*)$'
    dat=re.findall(reg, d)
    #dat1=(re.search(reg, d).group())


print('Введенная дата',dat)
print()
print()
print('Задание 2')
