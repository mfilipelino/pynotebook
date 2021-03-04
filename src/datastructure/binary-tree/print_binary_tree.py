from node import Node


def print_inorder(node):
    if node:
        print_inorder(node.left_child)
        print(node.element)
        print_inorder(node.right_child)


def print_posorder(node):
    if node:
        print_posorder(node.left_child)
        print_posorder(node.right_child)
        print(node.element)


def print_preorder(node):
    if node:
        print(node.element)
        print_preorder(node.left_child)
        print_preorder(node.right_child)


def test_base():
    print()
    print_posorder(None)


def test_base_one_element():
    print()
    print_posorder(Node(1))


def test_base_two():
    print()
    root = Node(1)
    root.add_right(Node(2))
    root.add_left(Node(3))
    print()
    print_posorder(root)
    print()
    print_inorder(root)
    print()
    print_preorder(root)
