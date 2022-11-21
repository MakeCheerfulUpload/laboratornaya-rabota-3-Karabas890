import re
text=input("Ввдите текст:")
pattern=r"(\w+)(\s+\1\b)+"
print(re.sub(pattern, r"\1", text))
