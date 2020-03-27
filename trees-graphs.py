from collections import deque

class DirectedNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

class DirectedGraph:
    def __init__(self, root):
        self.root = root

def is_route(node1, node2):
    queue = deque()
    visited = set()
    visited.add(node1)
    queue.append(node1)

    while len(queue) > 0:
        curr_node = queue.popleft()
        for node in curr_node.neighbors:
            if node not in visited:
                print(node.data)
                if node == node2:
                    return True
                visited.add(node)
                queue.append(node)

    queue = deque()
    visited = set()
    visited.add(node2)
    queue.append(node2)
    while len(queue) > 0:
        curr_node = queue.popleft()
        for node in curr_node.neighbors:
            if node not in visited:
                print(node.data)
                if node == node1:
                    return True
                visited.add(node)
                queue.append(node)
    
    return False

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.traversal_helper('', 0)

    def traversal_helper(self, output, height):
        if self.left:
            output += self.left.traversal_helper('', height + 1)
        output += f'({self.data}: {height}) '
        if self.right:
            output += self.right.traversal_helper('', height + 1)
        return output


# 1, 2, 3, 4, 5, 6, 7, 8, 9
def get_minimal_tree(lst):
    if len(lst) == 0:
        return None
    mid = len(lst) // 2
    node = TreeNode(lst[mid])
    node.left = get_minimal_tree(lst[:mid])
    node.right = get_minimal_tree(lst[mid+1:])
    return node

def get_depth_lists(root):
    def helper(node, depth_map, height):
        if node == None:
            return depth_map
        helper(node.left, depth_map, height + 1)
        if height in depth_map:
            depth_map[height].append(node.data)
        else:
            depth_map[height] = [node.data]
        helper(node.right, depth_map, height + 1)
        return depth_map

    depth_map = helper(root, {}, 0)
    return [depth_map[depth] for depth in depth_map]

def get_height_if_balanced(root):
    if root == None:
        return 0

    left_height = get_height_if_balanced(root.left)
    right_height = get_height_if_balanced(root.right)

    if left_height is None or right_height is None or abs(left_height - right_height) > 1:
        return None


    return max(left_height, right_height) + 1
    

def is_balanced(root):
    return get_height_if_balanced(root) is not None

def get_max_if_bst(node):
    if root == None:
        return 0
    
    left_max = get_max_if_bst(node)
    right_max = get_max_if_bst(node)

    is_subtree_bst = left_max is not None and right_max is not None
    is_bst = left_max <= node.data and right_max > node.data
    if not (is_subtree_bst and is_bst):
        return None

    return right_max


def is_bst(root):
    return get_max_if_bst(root) is not None

class TreeNodeParent:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

def get_minimal_tree_parent(lst):
    def helper(lst, parent):
        if len(lst) == 0:
            return None
        mid = len(lst) // 2
        node = TreeNodeParent(lst[mid], parent)
        node.left = helper(lst[:mid], node)
        node.right = helper(lst[mid+1:], node)
        return node
    return helper(lst, None)

def get_successor(node):
    cursor = node
    while cursor.data <= node.data and cursor.parent != None:
        print(cursor.data)
        cursor = cursor.parent
    return cursor.data

def get_build_order(projects, deps):
    projects = set(projects)
    nodes = {}
    for project in projects:
        nodes[project] = DirectedNode(project)

    for dep in deps:
        if dep[1] in projects:
            projects.remove(dep[1])
    
    try:
        start_project = projects.pop()
    except:
        return None

    roots = [nodes[project] for project in projects]
    print([root.data for root in roots])
    
    for dep in deps:
        dependent = nodes[dep[1]]
        dependee = nodes[dep[0]]
        if dependee.neighbors:
            dependee.neighbors.append(dependent)
        else:
            dependee.neighbors = [dependent]
        print(dependee.data, ':', [neighbor.data for neighbor in dependee.neighbors])

    visited = set()
    result = []
    for root in roots:
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            if node not in visited:
                print(node.data, [neighbor.data for neighbor in node.neighbors])
                visited.add(node)
                result.append(node.data)
                queue.extend(node.neighbors)
    return result

def search(root, node):
    if root == node:
        return True
    elif root == None:
        return False
    return search(root.left, node) or search(root.right, node)

def get_first_common_ancestor(root, node1, node2):
    if root == None:
        return None
    elif search(root.left, node1) and search(root.left, node2):
        return get_first_common_ancestor(root.left, node1, node2)
    elif search(root.right, node1) and search(root.right, node2):
        return get_first_common_ancestor(root.right, node1, node2)
    return root

def get_permutations(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]

    permutations = []
    for i, elem in enumerate(lst):
        remaining = lst[:i] + lst[i+1:]
        for permutation in get_permutations(remaining):
            permutations.append([elem] + permutation)
        
    return permutations

def is_equal(node1, node2):
    if node1 is not node2:
        return False
    if node1 is None and node2 is None:
        return True
    return is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)

def is_subtree(node1, node2):
    if node1 is None or node2 is None:
        return False
    if node1 is node2:
        return is_equal(node1, node2)
    return is_subtree(node1.left, node2) or is_subtree(node1.right, node2)
    

if __name__ == '__main__':
    root = get_minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(is_subtree(root.left, root.right.right))
   