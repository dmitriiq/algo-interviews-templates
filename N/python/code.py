from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.neighbours = []

visited_nodes = dict()

def cloneGraph(node) -> Node:
    # Your code
    # “ヽ(´▽｀)ノ”
    if node.val in visited_nodes:
        return visited_nodes[node.val]

    new_head = Node(node.val)
    visited_nodes[new_head.val] = new_head
    for n in node.neighbours:
        new_head.neighbours.append(cloneGraph(n))

    return new_head
