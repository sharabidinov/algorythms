# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num_of_letter = int(input('Введите номер буквы (1-26): '))

abc = list(map(chr, range(ord('a'), ord('z')+1)))

print(abc[num_of_letter-1])
