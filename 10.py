str = str(input('Enter a string: '))

#Print the length of the string.
print(len(str))

#Change the string to uppercase format.
print(str.upper())

#Change the string to lowercase format.
print(str.lower())

#Print the 2nd character of the string.
print(str[1])

#Insert the string "IN" between the first character and the second character of the string.
print(str[:1] + 'IN' + str[1:])

#Check if the letter "s" is in the string.
if 's' in str:
    print('Yes')