a = 5
list = ''
for i in range(a, 0, -1):
    if i == 1:
        list += str(i)
    else:
        list += str(i) + ', '
print(list)
    
while a >= 1:
    if a == 1:
        list += str(a)
    else:
        list += str(a) + ', '
    a -= 1
    
print(list)