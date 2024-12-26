while True:
    A = int(input("Enter a non-negative integer: "))
    if A >=5 and A <= 10:
        print("The number is between 5 and 10")
        break
    else:
        print("The number is not between 5 and 10")
        continue