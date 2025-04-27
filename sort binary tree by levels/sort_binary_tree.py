"""
Sorting binary tree by levels
"""

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

class Queue:
    """
    Data structure queue.
    """
    def __init__(self):
        """
        Data initiializer for queue
        """
        self.queue = []

    def push(self, x):
        """
        Adding element to queue
        :param x: element to be added
        """
        self.queue.append(x)

    def peek(self):
        """
        Returns the top item of the queue.

        :return: The top item of the stack.
        """
        if self.queue:
            return self.queue[0]

    def pop(self):
        """
        Removing element from queue
        """
        if not self.queue:
            return None
        return self.queue.pop(0)

    def __len__(self):
        """
        Getting length of queue
        :return: int,  length of queue
        """
        return len(self.queue)

    def empty(self):
        """
        Checking if queue is empty

        :return: bool, empty of full
        """
        return len(self.queue) == 0

    def __str__(self):
        """
        Returns a string representation of the queue.

        :return: A string representing the queue.
        """
        return str(self.queue)

def tree_by_levels(node):
    """
    BFS
    """
    if node is None:
        return []

    nodes_to_visit = Queue()
    nodes_to_visit.push(node)
    visited = []

    while nodes_to_visit:
        curr_node = nodes_to_visit.pop()
        if curr_node not in visited:
            visited.append(curr_node.value)

            if curr_node.left and curr_node.left not in visited:
                nodes_to_visit.push(curr_node.left)

            if curr_node.right and curr_node.right not in visited:
                nodes_to_visit.push(curr_node.right)
    return visited
