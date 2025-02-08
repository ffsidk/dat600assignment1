import time
import sys

sys.setrecursionlimit(10**6)


def insertion_sort(A, i=None):
    if i is None:
        i = len(A) - 1
    if i > 0:
        insertion_sort(A, i - 1)
        insert_last(A, i)


def insert_last(A, i):
    if i > 0 and A[i] < A[i - 1]:
        A[i], A[i - 1] = A[i - 1], A[i]
        insert_last(A, i - 1)


if __name__ == "__main__":
    sizes = [10, 50, 100, 500, 1000, 10000, 20000]
    for size in sizes:
        arr = list(range(size, 0, -1))  # Reverse-sorted array
        start_time = time.perf_counter()
        insertion_sort(arr)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        print(f"Size: {size}, Time taken: {time_taken:.6f} seconds")

    # Print results
    # for size, time_taken in zip(sizes, times):
    #     print(f"Size: {size}, Time taken: {time_taken:.6f} seconds")
    # arr = random.sample(range(size * 10), size)
    # reverse sorted array so we get the worst case
    # arr = list(range(size, 0, -1))
    # worst case is reverse sorted
