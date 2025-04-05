class TreeSort:
    
    class Node:
        def __init__(self, value):
            self.left = self.right = None
            self.value = value
    
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if not root:
            return self.Node(value)
        if value[1] < root.value[1]:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root
    
    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.value)
            self.inorder_traversal(root.right, result)
    
    def tree_sort(self, arr):
        self.root = None
        for item in arr:
            self.root = self.insert(self.root, item)
        sorted_arr = []
        self.inorder_traversal(self.root, sorted_arr)
        return sorted_arr