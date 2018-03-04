#Task4 Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.

sum = 0
for i in range(10):
    a = int(input("Enter number: "))
    sum = sum + a

print(sum)