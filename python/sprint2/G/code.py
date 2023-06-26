test_com = ['get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop', 'get_max', 'get_max']
test_com1 = ['get_max', 'pop', 'pop', 'pop', 'push 10', 'get_max', 'push -9']

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            initial_items = self.items * 1
            max = initial_items.pop()
            while len(initial_items) != 0:
                item = initial_items.pop()
                if item > max:
                    max = item
            print(max)
        else: print(None)

    def __str__(self):
        return str(self.items)


def read_input():
    n = int(input())
    #commands = [test_com1[i].strip().split() for i in range(n)]
    commands = [input().strip().split() for i in range(n)]
    return commands


def solution(commands):
    stack = StackMax()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            stack.pop()
        else: stack.get_max()


solution(read_input())
# if __name__ == '__main__':
#     solution(read_input())
