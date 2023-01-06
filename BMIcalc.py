firstName = input("Please enter first name: ")
lastName = input("Please enter last name: ")
weight = int(input("Please enter your weight: "))
height = int(input("Please enter your height: "))

BMI =round(weight / (height/100)**2, 2)


if BMI < 18.5:
    statusBody = "Underweight"
elif BMI < 24.9:
    statusBody = "Healthy weight"
elif BMI <29.9:
    statusBody = "Overweight"
else:
    statusBody = "Obesity"


print("HI", firstName, lastName)
print("your height is",height,"Cm","and your weight is",weight,"Kg")
print("your BMI is",BMI,"and your weight status is",statusBody)
