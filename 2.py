# Take input from the user
A = int(input("Enter a non-negative integer: "))

# Print all even numbers from 0 to A
for i in range(0, A+1, 1):
    if i % 2 == 0 or i == A:
        print(i)