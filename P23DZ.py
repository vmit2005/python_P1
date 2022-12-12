import re
print('Задание 1')
s="1X, Text ABC 123 A1B2C3"
reg=r'(\d)[A-Za-z]'

#print(re.findall(reg,s))
print(re.findall(reg,s+"A"))

print()
print()
print("Задание 2")
s="text from #START# till #END#"
reg=r'(?<=#START#).*?(?=#END#)'
print(re.findall(reg,s))

print()
print()
print("Задание 3")

s="12_34__56"
reg=r'\d{2}_(?!_)'
print(re.findall(reg,s))





