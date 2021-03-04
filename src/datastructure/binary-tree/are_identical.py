from node import Node


def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return (root1.data == root2.data) and \
               are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)
    else:
        return False


def test_base():
    assert are_identical(None, None) is True
    assert are_identical(Node(1), Node(2)) is False


def test_six():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    assert are_identical(node1, node1) is True
    assert are_identical(node1, node2) is False