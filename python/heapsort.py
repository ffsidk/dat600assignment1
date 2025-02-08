import math


def max_heapify(A, n, i):
    # called log2(n) times
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    steps = 3

    if left < n and A[left] > A[largest]:
        steps += 1
        largest = left

    if right < n and A[right] > A[largest]:
        steps += 1
        largest = right

    if largest != i:
        steps += 1
        A[i], A[largest] = A[largest], A[i]
    return steps


def build_max_heap(A):
    steps = 0
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        # print(f"i in build heap: {i}")
        # called (len(n) // 2) - 1 times
        steps += 1
        steps += max_heapify(A, n, i)
    return steps


def heap_sort(A):
    steps = 0
    n = len(A)

    steps += build_max_heap(A)

    for i in range(n - 1, 0, -1):
        steps += 1
        # print(f"i in heap_sort: {i}")
        A[i], A[0] = A[0], A[i]
        steps += 1
        steps += max_heapify(A, i, 0)
    return steps


if __name__ == "__main__":
    size = 100
    # arr = random.sample(range(size * 10), size)
    # reverse sorted array so we get the worst case
    arr = list(range(size, 0, -1))
    wanted_steps = size * math.log(size, 2)
    print(arr)
    print(f"wanted steps: {wanted_steps}")
    steps = heap_sort(arr)
    print(f"Steps taken: {steps}")
    print("Sorted array:", arr)
