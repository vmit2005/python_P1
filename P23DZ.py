import re
print('Задание 1')
s="1X, Text ABC 123 A1B2C3"
reg=reg= r'(\d)[A-z]'

#print(re.findall(reg,s))
print(re.findall(reg,s+"A"))
print(re.sub(reg,"", s))