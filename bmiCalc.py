print("THIS IS BMI CALCULATOR")

print("enter your Height: ")
height = int(input()) / 100
print("enter your Weight: ")
weight = int(input())

BMI = weight / height ** 2

print("your BMI is: ")
print(round(BMI, 1))

if BMI < 18.5:
    Print("youre underweight")
elif BMI < 24.6:
    print("youre normal Weight")
elif BMI < 29.9:
    print("Youre overweight")
else: 
    print("obesity")
