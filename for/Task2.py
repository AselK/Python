#Task2 Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a < b:
    for q in range (a, b + 1):
        print(q)
else:
    for q in range (a, b - 1, -1):
        print(q)
