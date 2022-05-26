class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop()


q = Queue()
exp = input('Please enter the expression: ')


for c in exp:
    if c == '(':
        q.enqueue(1)
        if c == ')':
            if q.is_empty():
                is_balanced = False
                break
            q.pop()



else:
    if q.is_empty():
        is_balanced = True
    else:
        is_balanced = False

if is_balanced:
    print('Expression ', exp, ' is correctly parenthesized.')
else:
    print('Expression ', exp, ' is not correctly parenthesized.')
