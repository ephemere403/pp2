#ws3 Strings
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]
#first letter

txt = "Hello World"
x = txt[2:5]
#letters from 3rd to 5th "llo"

txt = " Hello World "
x = txt.strip()

txt = " Hello World "
x = txt.upper()

txt = " Hello World "
x = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))