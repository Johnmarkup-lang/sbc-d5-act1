l = []
l.append(int(input("butang number: "))); l.append(int(input("butang number: "))); l.append(int(input("butang number: "))); l.append(int(input("butang number: "))); l.append(int(input("butang number: ")))
#e.g: 1 2 3 4
#     0 1 2 3
print ("DISPLAY INPUTTED NUMBERS: ", l)
head = input("naa si boss? (oo/wala): ")

if head == 'oo':
    l.pop(0)
else:
    l.pop()
print(l)
