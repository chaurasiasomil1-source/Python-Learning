age = int(input("enter your age:\n"))


if age >= 18 and age <=24 :
    print("age eligible")

    marks = int(input("enter your marks:\n"))

    if marks > 75 :
        print("age + marks -> you are eligible for admission")
    else :
        print("your age eligible but marks not enough for admission")


else:
 print("age not eligible because of your age")