#Task1 Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a <= b:
     for q in range(a, b + 1):
        print(q)
