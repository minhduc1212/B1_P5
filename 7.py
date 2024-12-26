#Input three positive integers a, b, c, print the largest number out of those 3 numbers.
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))
if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
else:
    print(C)