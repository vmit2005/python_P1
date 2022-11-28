import re
print('Задание 1')
s="1X, Text ABC 123 A1B2C3"
reg=r'[\w\s]{2;}'
#print(re.findall(reg,s))
print(re.findall(reg,s))
print(re.sub(reg,"", s))