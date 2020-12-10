class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def get_head(self):
        return self.head_node

    def get_tail(self):
        return self.tail_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert(self, Node):
        if self.is_empty():
            self.head_node = Node
            self.tail_node = Node
        else:
            self.tail_node.next_element = Node
            self.tail_node = Node


    # Supplementary print function
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list


def insert_at_tail(lst, value):
    lst.insert(Node(value))


def test_base():
    lst = LinkedList()
    assert lst.is_empty() == True
    assert lst.get_head() == None


def test_insert():
    lst = LinkedList()
    lst.insert(Node(1))
    assert lst.get_head().data == 1
    lst.insert(Node(2))
    assert lst.get_head().data == 1
    assert lst.get_tail().data == 2
    lst.insert(Node(3))
    assert lst.get_tail().data == 3


def test_print():
    lst = LinkedList()
    lst.insert(Node(1))
    lst.insert(Node(2))
    lst.insert(Node(3))
    lst.print_list()

