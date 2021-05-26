value = int(input("Enter intial value:"))

while (value >= 0):
    remove = int(input("To remove:"))
    value = value - remove
    if value >= 0 :
        print(value)
    else :
        print('0')