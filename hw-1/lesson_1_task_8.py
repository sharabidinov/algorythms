# Определить, является ли год, который ввел пользователь, високосным или не високосным.
year = int(input('Введите год: '))

if year % 4 == 0 or year % 4 == 0:
    print(f'{year} високосный год')
else:
    print(f'{year} не високосный год')
