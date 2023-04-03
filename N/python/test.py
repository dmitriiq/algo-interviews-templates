from code import cloneGraph
from node import Node

node = Node(33)

node.neighbours.append(Node(34))
node.neighbours.append(Node(35))
node.neighbours.append(Node(36))
node.neighbours.append(Node(37))

new_anode = cloneGraph(node)

def print_node(node: Node):
    print(node.val)
