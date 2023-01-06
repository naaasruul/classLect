num1 = int(input("enter any Number: "))
num2 = int(input("enter any Number:"))

# print("choose operation:")
print("Menu:")
print("1.ADD")
print("2.MULTIPLY")

print("choose operation in the menu:")
operation = int(input())

if operation == 1:
    print("total: ", num1 + num2)
elif operation == 2:
    print("total: ", num1 * num2)
else:
    print("not an option")