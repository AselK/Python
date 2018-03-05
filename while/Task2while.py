#Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

number = int(input("Enter number: "))
i = 2
while i <= number:
    if number % i == 0:
        print(i)
        break
    i += 1