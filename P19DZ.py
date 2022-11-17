s='Заментите  в этой строке все появления буквы о на букву "О", кроме первого и последнего вхождения '

d=[]
for i in range(len(s)):
    if s[i]=='о':
        d.append(i)
d=d[1:-1]
for i in d:
    s1=s[:i]+"O"+s[i+1:]
print(s1)
#******************************
i1=s.find('о')
i2=s.rfind('о')
s1=s[:i1+1]
s3=s[i2:]
s2=s[i1+1:i2].replace('о','O')
print(s1+s2+s3)

print(s2.join([s1,s3]))
#***********************************
s1=s.split('о')
s2=""
for i in range(len(s1)):
    if i==0 or i==len(s1)-2:
        s2+=s1[i]+'о'
    elif i==len(s1)-1:
        s2+=s1[i]
    else:
        s2+=s1[i]+"О"

print(s2)