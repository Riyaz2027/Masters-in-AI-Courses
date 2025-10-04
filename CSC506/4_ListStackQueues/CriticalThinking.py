
from collections import deque
import random
import time
import pandas as pd

class LIFOStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0
    

class FIFOQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0



def generate_inputs(n, mode="sequential"):
    if mode == "sequential":
        return list(range(1, n+1))
    elif mode == "random":
        return [random.randint(1, n) for i in range(n)]
    elif mode == "duplicates":
        return [random.choice([1, 2, 3, 4, 5]) for i in range(n)]
    else:
        return []


def test_algorithm(data, structure_type="LIFO"):
    if structure_type == "LIFO":
        s = LIFOStack()
        start = time.time()
        for item in data:
            s.push(item)
        popped = []
        while not s.is_empty():
            popped.append(s.pop())
        end = time.time()
    else:
        q = FIFOQueue()
        start = time.time()
        for item in data:
            q.enqueue(item)
        popped = []
        while not q.is_empty():
            popped.append(q.dequeue())
        end = time.time()

    return {
        "input_size": len(data),
        "execution_time": end - start,
        "output_sample": popped[:10]  # first 10 items
    }

# Generate inputs - Riyaz
seq_input = generate_inputs(10000, "sequential")
rand_input = generate_inputs(10000, "random")

# Test LIFO - Riyaz
lifo_seq = test_algorithm(seq_input, "LIFO")
lifo_rand = test_algorithm(rand_input, "LIFO")

# Test FIFO - Riyaz
fifo_seq = test_algorithm(seq_input, "FIFO")
fifo_rand = test_algorithm(rand_input, "FIFO")

results = pd.DataFrame([lifo_seq, lifo_rand, fifo_seq, fifo_rand])
print(results)

