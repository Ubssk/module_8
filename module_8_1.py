def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))    # вывод: 123.456строка
print(add_everything_up('яблоко', 4215))       # вывод: яблоко4215
print(add_everything_up(123.456, 7))           # вывод: 130.456