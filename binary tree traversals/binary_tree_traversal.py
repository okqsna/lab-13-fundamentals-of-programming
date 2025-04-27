class Node:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node, nodes = None):
    if node is None:
        return []

    if nodes is None:
        nodes = []

    nodes.append(node.data)
    pre_order(node.left, nodes)
    pre_order(node.right, nodes)

    return nodes

# In-order traversal
def in_order(node, nodes = None):
    if node is None:
        return []

    if nodes is None:
        nodes = []

    in_order(node.left, nodes)
    nodes.append(node.data)
    in_order(node.right, nodes)

    return nodes

# Post-order traversal
def post_order(node, nodes = None):
    if node is None:
        return []

    if nodes is None:
        nodes = []

    post_order(node.left, nodes)
    post_order(node.right, nodes)
    nodes.append(node.data)

    return nodes
