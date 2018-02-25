# Can king move from first position to the second position

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

if ((x1 == x2 - 1) or (x1 == x2) or (x1 == x2 + 1)) and ((y1 == y2 -1) or (y1 == y2) or (y1 == y2 +1)):
    print("Yes")
else:
    print("No")