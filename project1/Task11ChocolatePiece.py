# Can you break chocolate into two part

n = int(input("Enter n: "))
m = int(input("Enter m: "))
k = int(input("Enter k: "))

if ((k < n * m) and (not ((k < m) and (k < n)))
        and ((k % n == 0) or (m % n == 0))):
    print("Yes")
else:
    print("No")