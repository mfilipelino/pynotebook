class MyStack(object):
    def __init__(self):
        self.stack_list = []

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        return self.stack_list.pop()

    def is_empty(self):
        return self.stack_list == []

    def top(self):
        if self.is_empty():
            print('is empty')
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def test_is_empty():
    stack = MyStack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False
    stack.pop()
    assert stack.is_empty() == True


def test_push():
    stack = MyStack()
    stack.push(1)
    stack.push(1)
    stack.push(1)
    assert stack.size() == 3


def test_pop():
    stack = MyStack()
    stack.push(1)
    stack.pop()
    assert stack.size() == 0


def test_top():
    stack = MyStack()
    stack.top()
    stack.push(1)
    assert stack.top() == 1