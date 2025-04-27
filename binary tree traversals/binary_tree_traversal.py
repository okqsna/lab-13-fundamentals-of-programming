class Node:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node, nodes = []):
    if node is None:
        return []

    nodes.append(node.data)
    pre_order(node.left)
    pre_order(node.right)

    return nodes

# In-order traversal
def in_order(node, nodes = []):
    if node is None:
        return []

    in_order(node.left)
    nodes.append(node.data)
    in_order(node.right)

    return nodes

# Post-order traversal
def post_order(node, nodes = []):
    if node is None:
        return []

    post_order(node.left)
    post_order(node.right)
    nodes.append(node.data)

    return nodes
