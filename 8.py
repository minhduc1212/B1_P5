A = int(input("Enter a number: "))
B = int(input("Enter a number: "))

if A == B:
    print("The numbers are equal")
elif A > B:
    print("The numbers from B to A are:")
    for i in range(B, A+1):
        print(i)
else:
    print("The numbers from A to B are:")
    for i in range(A, B+1):
        print(i)