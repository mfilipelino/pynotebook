from LinkedList import LinkedList


def detect_loop(lst):
    if lst.is_empty():
        return False
    else:
        dit = {}
        node = lst.get_head()
        while node.next_element:
            if node.data in dit:
                return True
            else:
                dit[node.data] = True
            node = node.next_element
        return False


def test_base():
    lst = LinkedList()
    assert detect_loop(lst) is False


def test_one_element():
    lst = LinkedList()
    lst.insert_at_head(1)
    assert detect_loop(lst) is False


def test_loop_basic():
    lst = LinkedList()
    lst.insert_at_head(1)
    lst.insert_at_head(1)
    assert detect_loop(lst) is True


def test_loop_basic():
    lst = LinkedList()
    lst.insert_at_head(1)
    lst.insert_at_head(3)
    assert detect_loop(lst) is False