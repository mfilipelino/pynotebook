from Node import Node
from LinkedList import LinkedList


def reverse(lst):
    new_list = LinkedList()

    while not lst.is_empty():
        node = lst.get_head()
        lst.delete_at_head()
        new_list.insert_at_head(node.data)
    return new_list


def test_base():
    print()
    lklst = LinkedList()
    lklst.insert_at_head(1)
    lklst.insert_at_head(2)
    lklst.insert_at_head(3)
    lklst.print_list()
    reverse(lklst).print_list()
