x = int(input("please insert your number: "))

if x%2 == 0:
    if x<0:
        print(x, "is even and negative!")
    else:
        print(x, "is even and positive")
else:
    if x<0:
        print(x, "is odd and negative")
    else:
        print(x, "is odd and positive")

# OR u can use this method

# if x<0 and x%2==0:
#     print(x, "is negative and even")
# else:
    

