# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

num_of_letter = int(input('Введите номер буквы (1-26): '))

abc = string.ascii_lowercase

print(abc[num_of_letter-1])
