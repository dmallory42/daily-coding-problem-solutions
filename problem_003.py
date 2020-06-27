# ---------------------------
# Problem 3
# Given the root to a binary tree, implement serialize(root), which serializes the tree
# into a string, and deserialize(s), which deserializes the string back into the tree.
# ---------------------------


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(s: str):
    def decode(vals):
        val = next(vals)

        if val == '#':
            return None

        return Node(str(val), decode(vals), decode(vals))

    vals = iter(s.split(', '))
    return decode(vals)


def serialize(root: Node):
    vals = []

    def encode(node: Node):
        if node is not None:
            vals.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            # # used to represent a child node not existing (used to maintain structure)
            return vals.append('#')

    encode(root)
    return ', '.join(vals)


node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'
