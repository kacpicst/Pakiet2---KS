numbers = [5, 10, 15, 20, 25]

squared_greater_than_10 = [square for num in numbers if (square := num ** 2) > 10]

print(squared_greater_than_10)
