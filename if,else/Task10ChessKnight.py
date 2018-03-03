# Can knight move from first position to the second position

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

if (((x1 - x2 == 2) and (y1 - y2 == -1)) or ((x1 - x2 == 1) and (y1 - y2 == -2))
        or ((x1 - x2 == -1) and (y1 - y2 == -2)) or ((x1 - x2 == -2) and (y1 - y2 == -1))
        or ((x1 - x2 == -2) and (y1 - y2 == 1)) or ((x1 - x2 == -1) and (y1 - y2 == 2))
        or ((x1 - x2 == 1) and (y1 - y2 == 2)) or ((x1 - x2) and (y1 - y2 == 1))):
    print ("Yes")
else:
    print("No")