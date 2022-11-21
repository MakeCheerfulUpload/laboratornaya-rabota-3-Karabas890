import re
text=input("Ввдите текст:")
pattern=r"(\d+\b)"
pattern1=r"(\d+\b)"

m=(re.findall(pattern, text))
k=(re.findall(pattern, text))
for i in range (len(m)):
    m[i]=str((int(m[i])**2)*4-7)
    #print(m[i])


for j in range (len(m)):
    
    text=(re.sub(k[j],m[j],text))
print(text)
    

