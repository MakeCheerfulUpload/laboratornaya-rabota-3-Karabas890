import re
text = input("Введите текст:")
print(len(re.findall(";<\{/", text)))
