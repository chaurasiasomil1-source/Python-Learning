name = input("what is your name ?\n")
age = int(input("how old are you\n"))

if age >=18:
    print(name, "you are a adult")
elif 13 <= age <= 17:
    print(name, "you are a teenager")
else:
    print(name, "you are a child")