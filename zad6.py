def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Wystąpił błąd podczas wywoływania funkcji: {func.__name__}. Błąd: {e}")
            return None
    return wrapper

@safe_function
def divide(a, b):
    return a / b

result = divide(10, 2)
print("Wynik dzielenia:", result)

result = divide(10, 0)  # Powinien pojawić się komunikat o błędzie
print("Wynik dzielenia:", result)
