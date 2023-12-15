import collections

class Node:
    def __init__(self, data, hd=0):  # Include a default value for hd
        self.data = data
        self.left = None
        self.right = None
        self.hd = hd  # horizontal distance from root

def verticalOrder(root):
    if not root:
        return []

    hd_map = collections.defaultdict(list)  # key: hd, value: list of nodes

    q = collections.deque([(root, 0)])  # queue with (node, hd)
    min_hd = float('inf')  # minimum horizontal distance
    max_hd = -float('inf')  # maximum horizontal distance

    # Perform level-order traversal with horizontal distance tracking
    while q:
        node, hd = q.popleft()
        hd_map[hd].append(node.data)  # add node data to its hd level
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            q.append((node.left, hd - 1))  # add left child with updated hd
        if node.right:
            q.append((node.right, hd + 1))  # add right child with updated hd

    # Build vertical traversal list from hd_map
    vertical_traversal = []
    for hd in range(min_hd, max_hd + 1):
        vertical_traversal.extend(hd_map[hd])

    return vertical_traversal

# Explanation of Vertical Traversal:
#      
#         1
#       /    \
#      2      3
#    /  \   /  \
#   4    5 6    7
#            \    \
#             8    9 
#
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.left.left = Node(9)

# Call the verticalOrder function
vertical_traversal = verticalOrder(root)

# Print the result
print("Vertical order traversal:", vertical_traversal)
