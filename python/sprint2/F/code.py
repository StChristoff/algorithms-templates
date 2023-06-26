test_com = ['get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop', 'get_max', 'get_max']

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item:
            self.items.append(int(item))

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def get_max(self):
        if self.items:
            print(max(abs(self.items)))
        print(None)
    
    def execute(self, command, arg=None):
        print(f'--command={command}, arg={arg}')
        COMMANDS = {
            'push': self.push(arg),
            'pop': self.pop(),
            'get_max': self.get_max(),
        }
        COMMANDS[command]
        return self

    def __str__(self):
        return str(self.items)


def read_input():
    n = int(input())
    stack = Stack()
    for i in range(n):
       command = test_com[i].strip().split()
       #command = input().strip().split()
       print(f'---command = {command}')
       stack.execute(*command)


if __name__ == '__main__':
    read_input()
