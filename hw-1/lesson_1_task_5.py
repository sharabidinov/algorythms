# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
print('Введите две буквы от a до z')

letter_1 = input('1-я буква: ')
letter_2 = input('2-я буква: ')

abc = list(map(chr, range(ord('a'), ord('z')+1)))

# У нас идеальный пользователь который сначала водит буквы по порядку в алфавите)
place_letter_1 = abc.index(letter_1) + 1
place_letter_2 = abc.index(letter_2) + 1
letter_between = (abc.index(letter_2) - abc.index(letter_1)) - 1

print(abc)
print(f'{letter_1} {place_letter_1}-я буква в алфавите')
print(f'{letter_2} {place_letter_2}-я буква в алфавите')
print(f'между {letter_1} и {letter_2} {letter_between} букв')
