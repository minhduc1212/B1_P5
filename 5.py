#Input one positive integer A from the keyboard (0<A<10), print the multiplication table of A.
list = [1,2,3,4,5,6,7,8,9]
A = int(input("Enter a number: "))
if A >= 0 and A < 10:
    for i in list:
        print(A, "x", i, "=", A*i)