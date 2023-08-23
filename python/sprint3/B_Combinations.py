"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв.
Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно.
Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.

Пример 1
Ввод	Вывод
23
        ad ae af bd be bf cd ce cf
Пример 2
Ввод	Вывод
92
        wa wb wc xa xb xc ya yb yc za zb zc
"""

def сombinations(digits):
    keyboard = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'
                }
    def backtrack(digits, path, result):
        if digits == '':
            result.append(path)
            return
        for letter in keyboard[digits[0]]:
            path += letter
            backtrack(digits[1:], path, result)
            path = path[:-1]
    result = []
    backtrack(digits, '', result)
    for x in result:
        print(x, end=' ')
input_string = (input())
сombinations(input_string)
