# Ask the use for the distance to his country house, petrol consumption and price of the petrol per litre
# Print the cost of the ride back and forth

x = int(input("Enter distance: "))
y = int(input("Enter consumption litres/km: "))
z = int(input("Enter price: "))

print("Result is: " + str(x * z * y / 50))

