import time
import random

# --- Simple BST Implementation ---
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left: self.left.insert(key)
            else: self.left = BSTNode(key)
        elif key > self.key:
            if self.right: self.right.insert(key)
            else: self.right = BSTNode(key)

    def search(self, key):
        if self.key == key:
            return True
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        return False

# --- Simplified AVL Implementation ---
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(node): return node.height if node else 0

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

def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

def avl_insert(root, key):
    if not root: return AVLNode(key)
    if key < root.key: root.left = avl_insert(root.left, key)
    elif key > root.key: root.right = avl_insert(root.right, key)
    else: return root
    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)
    if balance > 1 and key < root.left.key: return rotate_right(root)
    if balance < -1 and key > root.right.key: return rotate_left(root)
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

# --- Empirical Test ---
def test_performance(tree_type, n=5000):
    nums = random.sample(range(1, n * 10), n)
    start = time.time()

    if tree_type == 'BST':
        root = BSTNode(nums[0])
        for num in nums[1:]:
            root.insert(num)
        for _ in range(1000):
            root.search(random.choice(nums))

    elif tree_type == 'AVL':
        root = None
        for num in nums:
            root = avl_insert(root, num)

    end = time.time()
    return end - start

print("BST Time:", test_performance('BST'))
print("AVL Time:", test_performance('AVL'))
