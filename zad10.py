def concat_strings(*args):
    return ' '.join(args)

# Przykładowe użycie funkcji
strings1 = "To", "jest", "zwykły", "test", "projektu"
strings2 = "Hello", "world"
strings3 = "This", "is", "a", "test"

# Testowanie funkcji na kilku zestawach stringów
print(concat_strings(*strings1))
print(concat_strings(*strings2))
print(concat_strings(*strings3))
