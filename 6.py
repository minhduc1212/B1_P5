A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))

if A + B > C:
    print("A, B, C are the lengths of three sides of a triangle")
    if A == B and B == C:
        print("The triangle is equilateral")
    elif A == B or B == C or A == C:
        print("The triangle is isosceles")
    elif A**2 + B**2 == C**2:
        print("The triangle is square")
    else:
        print("The triangle is scalene")
else:
    print("A, B, C are not the lengths of three sides of a triangle")