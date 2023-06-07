from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    num_days = len(temperatures)
    if num_days == 1:
        # print(f'--num_days == 1')
        return 1
    if (abs(temperatures[num_days-1])
        > abs(temperatures[num_days-2])):
        # print(f'--i[max]={temperatures[num_days-1]}')
        # print(f'--i[max]-1={temperatures[num_days-2]}')
        count += 1
        # print(f'--i[max]>i[max]-1, count={count}')
    if num_days == 2:
        # print(f'--num_days == 2, count={count}')
        return count
    if abs(temperatures[0]) > abs(temperatures[1]):
        count +=1
        # print(f'--i[1]>i[0], count={count}')
    for i in range(1, num_days-2):
        if abs(temperatures[i-1]) < abs(temperatures[i]) > abs(temperatures[i+1]):
            count += 1
            # print(f'--i[i-1]={temperatures[i-1]} < i[i]={temperatures[i]} > i[i+1]={temperatures[i+1]}')
            # print(f'--Условие выполнилось: count={count}')
    return count

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
