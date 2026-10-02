name = input("what is your name?\n")
marks = int(input("enter your marks\n"))

if marks > 90:
    print(name, "you got A grade")

elif marks < 90 and marks > 75:
    print(name, "you got B grade")

elif marks < 75 and marks > 50:
    print(name, "you got C grade")

else:
    print(name, "you failed")