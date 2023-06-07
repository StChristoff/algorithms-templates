from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    result = ''
    dif = abs(len(first_number) - len(second_number))
    if len(first_number) > len(second_number):
        second_number = '0'*dif + second_number
    else:
        first_number = '0'*dif + first_number
    for i in range(len(first_number)):
        if first_number[i]== second_number[i] == '1':
            result += '1'

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
