def is_palindrome(line: str) -> bool:
    SYMBOLS = ('.',',','!','?',':',';',' ')
    line = line.lower()
    forward = ''
    backward = ''
    for i in range(len(line)):
        if line[i] not in SYMBOLS:
            forward += line[i]
        if line[(i+1)*(-1)] not in SYMBOLS:
            backward += line[(i+1)*(-1)]
    if  forward != backward:
        return False
    return True

print(is_palindrome(input().strip()))
