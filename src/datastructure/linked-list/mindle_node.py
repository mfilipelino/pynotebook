from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def div(n):
    if n % 2 == 0:
        return (n // 2) + 1
    else:
        return n // 2


def find_mid(lst):
    if lst.is_empty():
        return None
    else:
        count = div(lst.length())
        node = lst.get_head()
        for i in range(count):
            node = node.next_element
        return node.data


def test_base():
    print()
    lkl = LinkedList()
    assert find_mid(lkl) == None
    lkl.insert_at_head(21)
    assert find_mid(lkl) == 21
    lkl.insert_at_head(10)
    assert find_mid(lkl) == 10
    lkl.insert_at_head(14)
    lkl.insert_at_head(7)
    lkl.print_list()
    assert find_mid(lkl) == 14
