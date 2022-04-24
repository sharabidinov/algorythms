"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и строку целиком.
"""
from sys import getsizeof

user_input = input('Введите строку: ')


class CountSubstring:
    def __init__(self, string):
        self.string = string
        self.result = set()

    def count_substrings(self):

        for i in range(len(self.string)):
            for j in range(i + 1, len(self.string) + 1):
                if self.string[i:j] == '' or self.string[i:j] != self.string:
                    self.result.add(self.string[i:j])

        print(self.result)
        return len(self.result)


test = CountSubstring(user_input)
print(test.count_substrings())
