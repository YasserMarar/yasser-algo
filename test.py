import random
import time
from typing import List

# Insertion Sort
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Quick Sort
def quick_sort(arr: List[int], low: int, high: int):
    while low < high:
        if high - low < 10:
            insertion_sort_subarray(arr, low, high)
            break
        else:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                quick_sort(arr, low, pivot_index - 1)
                low = pivot_index + 1
            else:
                quick_sort(arr, pivot_index + 1, high)
                high = pivot_index - 1
    return arr

def partition(arr: List[int], low: int, high: int) -> int:
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort()
    pivot_value, pivot_index = pivot_candidates[1]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low
    for j in range(low, high):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def insertion_sort_subarray(arr: List[int], low: int, high: int):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Benchmarking Function
def benchmark_sort(sort_name: str, sort_func, arr: List[int]):
    copied_arr = arr.copy()
    start = time.time()
    if sort_name == "Quick Sort":
        sort_func(copied_arr, 0, len(copied_arr) - 1)
    else:
        copied_arr = sort_func(copied_arr)
    end = time.time()
    print(f"{sort_name} | Size: {len(arr)} | Time: {end - start:.6f}s | Sorted: {copied_arr[:10]}...")

# Test All Sorts
def test_all_sorts():
    input_sizes = [10, 1000]
    input_types = {
        "Sorted": lambda n: list(range(n)),
        "Reversed": lambda n: list(range(n, 0, -1)),
        "Random": lambda n: random.sample(range(n * 2), n)
    }

    for size in input_sizes:
        for desc, generator in input_types.items():
            arr = generator(size)
            print(f"\n--- {desc} Input (n={size}) ---")
            benchmark_sort("Quick Sort", quick_sort, arr)
            benchmark_sort("Merge Sort", merge_sort, arr)
            if size <= 100:
                benchmark_sort("Insertion Sort", insertion_sort, arr)
            else:
                print("Skipping Insertion Sort for size > 100")

# Run the test
if __name__ == "__main__":
    test_all_sorts()

