"""
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно понять,
является ли первая из них подпоследовательностью второй. Когда строки достаточно длинные,
очень трудно получить ответ на этот вопрос, просто посмотрев на них. Помогите Гоше написать функцию,
которая решает эту задачу.

Формат ввода
В первой строке записана строка s.
Во второй —- строка t.
Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000.
Строки не могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.

Пример 1
Ввод	Вывод
abc
ahbgdcu
        True
Пример 2
Ввод	Вывод
abcp
ahpc
        False
"""

"""
Решение с рекурсией без сортировки:

def subseq(s, t):
    for i in range(len(t)):
        if s[0] == t[i]:
            if len(s) > 1:
                return subseq(s[1:], t[i+1:])
            return True
    return False


def input_seq():
    s = input()
    t = input()
    return s, t


print(subseq(*input_seq()))
"""

