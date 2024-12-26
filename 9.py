A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))

f_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
s_dict = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
t_dict = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

f = f_dict.get(A)
s = s_dict.get(B)
if B !=1:
    print(f + ' hundred ' + s + ' ' + f_dict.get(C))
else:
    print(f + ' hundred ' + t_dict.get(C))