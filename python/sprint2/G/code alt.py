test_com = ['get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop', 'get_max', 'get_max']
test_com1 = ['get_max', 'pop', 'pop', 'pop', 'push 10', 'get_max', 'push -9']

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.arr_max = [float('-inf'),]

    def push(self, item):
        self.items.append(item)
        if item >= self.arr_max[-1]:
            self.arr_max.append(item)

    def pop(self):
        if self.items:
            pop_item = self.items.pop()
            if pop_item == self.arr_max[-1]:
                self.arr_max.pop()
            return pop_item
        print('error')

    def get_max(self):
        if self.items:
            print(self.arr_max[-1])
        else:
            print(None)

    def __str__(self):
        return str(self.items)


def read_input():
    commands = [test_com[i].strip().split() for i in range(len(test_com))]
    # n = int(input())
    # commands = [input().strip().split() for i in range(n)]
    return commands


def solution(commands):
    stack = StackMaxEffective()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            stack.pop()
        else: stack.get_max()


solution(read_input())
# if __name__ == '__main__':
#     solution(read_input())
