# Can bishop move from first position to the second position

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

if abs(x1 - x2) == abs(y1 - y2):
    print("Yes")
else:
    print("No")
