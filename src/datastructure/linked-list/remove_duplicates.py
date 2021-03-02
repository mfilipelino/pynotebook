from LinkedList import LinkedList


def remove_duplicates(lst):
    if lst.is_empty():
        return lst
    else:
        node = lst.get_head()
        count_elements = set()
        count_elements.add(node.data)
        while node.next_element:
            node_next = node.next_element
            if node_next.data in count_elements:
                node.next_element = node_next.next_element
            else:
                count_elements.add(node_next.data)
                node = node.next_element
            if node is None:
                break

    return lst


def test_base():
    lst = LinkedList()
    assert remove_duplicates(lst).length() == 0


def test_one_element():
    lst = LinkedList()
    lst.insert_at_head(1)
    assert remove_duplicates(lst).length() == 1


def test_two_elements_duplicated():
    lst = LinkedList()
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(3)
    lst.insert_at_head(4)
    lst.insert_at_head(3)
    assert remove_duplicates(lst).length() == 3

