
class MyQueue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, element):
        if self.is_empty():
            return None
        else:
            self.queue_list.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue_list.pop(0)

    def is_empty(self):
        return self.queue_list == []

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.queue_list[-1]

    def back(self):
        if self.is_empty():
            return None
        else:
            return self.queue_list[0]

