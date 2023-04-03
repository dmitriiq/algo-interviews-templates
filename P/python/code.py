from typing import List, Optional


class Node:
    def __init__(self, i) -> None:
        self.left = None
        self.right = None
        self.i = i

result = []

def got_through(root: Node):
    if root.left != None:
        got_through(root.left)
    if root.right != None:
        got_through(root.right)
    if root.left == None and root.right == None:
        if not root.i in result:
            result.append(root.i)

def go_left(root: Node):
    if not root.i in result:
        result.append(root.i)
    if root.left != None:
        go_left(root.left)

def go_right(root: Node):
    if not root.i in result:
        result.append(root.i)
    if root.right != None:
        go_right(root.right)

def get_tree_border(root: Node) -> List[int]:
    # print('r i', root.i)
    got_through(root)
    go_left(root)
    go_right(root)

    return result

def read_tree() -> Node:
    size, root_id = map(int, input().split())
    nodes = [Node(i) for i in range(size)]
    for i in range(size):
        left, right = map(int, input().split())
        nodes[i].left = nodes[left] if left != -1 else None
        nodes[i].right = nodes[right] if right != -1 else None
    return nodes[root_id]


tree = read_tree()

s = ''
for t in get_tree_border(tree):
    s += str(t) + ' '
print(s)
