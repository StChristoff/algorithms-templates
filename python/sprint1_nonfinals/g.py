def to_binary(number: int) -> str:
    if number == 0:
        return 0
    b = ''
    while number > 0:
        b = str(number % 2) + b
        number = number // 2
    return int(b)

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
