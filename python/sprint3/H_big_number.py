"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел,
каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

Пример 1
Ввод	Вывод
3
15 56 2
        56215
Пример 2
Ввод	Вывод
3
1 783 2
        78321
"""


def is_first_card_weaker(card_1, card_2):  # функция-компаратор
    return int(card_1 + card_2) > int(card_2 + card_1)


def insertion_sort_by_comparator(array, more):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and more(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array)


def int_input():
    n = int(input())
    array = input().strip().split()
    return array


print(insertion_sort_by_comparator(int_input(), is_first_card_weaker))
