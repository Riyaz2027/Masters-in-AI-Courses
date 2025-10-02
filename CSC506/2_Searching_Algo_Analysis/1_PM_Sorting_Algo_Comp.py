import random
import time
import matplotlib.pyplot as plt

# ---------------- Sorting Algorithms ----------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# ---------------- measure the performance here ----------------
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start


# ---------------- Program starts here ----------------
if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000, 5000]
    bubble_times, merge_times, quick_times = [], [], []

    for n in sizes:
        test_data = [random.randint(1, 10000) for _ in range(n)]

        bubble_times.append(measure_time(bubble_sort, test_data))
        merge_times.append(measure_time(merge_sort, test_data))
        quick_times.append(measure_time(quick_sort, test_data))

    for i, n in enumerate(sizes):
        print(f"Size {n}: Bubble={bubble_times[i]:.6f}s, Merge={merge_times[i]:.6f}s, Quick={quick_times[i]:.6f}s")

    # Plot results
    plt.plot(sizes, bubble_times, label="Bubble Sort")
    plt.plot(sizes, merge_times, label="Merge Sort")
    plt.plot(sizes, quick_times, label="Quick Sort")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.show()
