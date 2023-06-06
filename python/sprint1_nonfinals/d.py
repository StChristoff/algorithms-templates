from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    if len(temperatures) == 1:
        return 1
    if (abs(temperatures[len(temperatures)-2])
        < abs(temperatures[len(temperatures)-1])):
        count += 1
    if len(temperatures) == 2:
        return count
    for i in range(1, len(temperatures)-2):
        if (abs(temperatures[i]) > abs(temperatures[i-1])
            and abs(temperatures[i]) > abs(temperatures[i+1])):
            count += 1
    return count

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
