from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

grouped_numbers = groupby(numbers, key=is_even)

for key, group in grouped_numbers:
    parity = "parzysta" if key else "nieparzysta"
    print(f"Liczba {parity}: {list(group)}")
