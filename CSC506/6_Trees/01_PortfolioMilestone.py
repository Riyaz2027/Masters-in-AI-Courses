import time
import random
import sys
sys.setrecursionlimit(10000)  # Prevent recursion depth errors

# --- Binary Search Tree Implementation ---
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BSTNode(key)
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BSTNode(key)

# --- AVL Tree Implementation ---
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_right(y):
    x, T2 = y.left, y.left.right
    x.right, y.left = y, T2
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def rotate_left(x):
    y, T2 = x.right, x.right.left
    y.left, x.right = x, T2
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def avl_insert(root, key):
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = avl_insert(root.left, key)
    elif key > root.key:
        root.right = avl_insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    # Balance the tree
    if balance > 1 and key < root.left.key:
        return rotate_right(root)
    if balance < -1 and key > root.right.key:
        return rotate_left(root)
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

# --- Performance Test ---
def test_performance(n=5000):
    # Sorted input = worst case for BST (degenerates into linked list)
    data = list(range(1, n + 1))

    # --- BST Timing ---
    start = time.time()
    root_bst = BSTNode(data[0])
    for num in data[1:]:
        root_bst.insert(num)
    bst_time = time.time() - start

    # --- AVL Timing ---
    start = time.time()
    root_avl = None
    for num in data:
        root_avl = avl_insert(root_avl, num)
    avl_time = time.time() - start

    print(f"BST Time: {bst_time:.5f} seconds")
    print(f"AVL Time: {avl_time:.5f} seconds")

test_performance()
