# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
digit = int(input('Введите трёхзначное число: '))
string = str(digit)


if len(string) == 3:
    num_1, num_2, num_3 = int(string[0]), int(string[1]), int(string[2])

    multiplication = num_1 * num_2 * num_3
    addition = num_1 + num_2 + num_3

    print(f'умножение = {multiplication}\ncумма = {addition}')
else:
    print('Вы ввели не трёхзначное число, попробуйте снова')
