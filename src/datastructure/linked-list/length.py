from LinkedList import LinkedList


def lenght(linked_lst):
    return linked_lst.lenght()


def test_base():
    lst = LinkedList()
    assert lst.lenght() is 0


def test_element_add():
    lst = LinkedList()
    lst.insert_at_tail(1)
    lst.insert_at_tail(2)
    assert lst.lenght() is 2