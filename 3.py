A = int(input("Enter a number: "))
def fractial(A):
    if A == 0:
        return 1
    else:
        return A * fractial(A-1)
print(fractial(A))
