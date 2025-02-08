import math


def insertion_sort(A, i=None):
    steps = 0
    if i is None:
        steps += 1
        i = len(A) - 1
        steps += 1
    if i > 0:
        steps += 1
        steps += insertion_sort(A, i - 1)
        steps += insert_last(A, i)
    return steps


def insert_last(A, i):
    steps = 0
    if i > 0 and A[i] < A[i - 1]:
        steps += 1
        A[i], A[i - 1] = A[i - 1], A[i]
        steps += 1
        steps += insert_last(A, i - 1)
    return steps


if __name__ == "__main__":
    size = 100
    # arr = random.sample(range(size * 10), size)
    # reverse sorted array so we get the worst case
    # arr = list(range(size, 0, -1))
    # worst case is reverse sorted
    arr = list(range(size, 0, -1))
    wanted_steps = size**2
    print(arr)
    print(f"wanted steps: {wanted_steps}")
    steps = insertion_sort(arr)
    print(f"Steps taken: {steps}")
    print("Sorted array:", arr)
