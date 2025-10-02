import time

# Bubble Sort algorithm - Riyaz
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["id"] > arr[j + 1]["id"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Merge Sort algorithm - Riyaz
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i]["id"] < right[j]["id"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    return arr

# we use the sample patient records to demonstrate the sorting algorithms
patients = [
    {"id": 5, "name": "Anna"},
    {"id": 3, "name": "Ben"},
    {"id": 8, "name": "Cathy"},
    {"id": 1, "name": "Dan"},
    {"id": 4, "name": "Eva"},
    {"id": 7, "name": "Frank"},
    {"id": 2, "name": "Grace"},
    {"id": 6, "name": "Hank"}
]

start_time = time.time()
bubble_sort(patients.copy())
end_time = time.time()
print("Time taken by Bubble Sort: {:.6f} seconds".format(end_time - start_time))

start_time = time.time()
merge_sort(patients.copy())
end_time = time.time()
print("Time taken by Merge Sort: {:.6f} seconds".format(end_time - start_time))


print("Bubble Sort:", bubble_sort(patients.copy()))
print("Merge Sort:", merge_sort(patients.copy()))
