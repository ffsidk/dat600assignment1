import math


def merge_sort(A, a=0, b=None):
    steps = 0
    if b is None:
        b = len(A)

    if 1 < b - a:
        c = (a + b + 1) // 2

        steps += merge_sort(A, a, c)
        steps += merge_sort(A, c, b)

        L, R = A[a:c], A[c:b]
        steps += merge(L, R, A, a, b)
    return steps


def merge(L, R, A, a, b):
    steps = 0
    i = j = 0
    k = a

    while i < len(L) and j < len(R):
        steps += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
        steps += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
        steps += 1

    return steps


if __name__ == "__main__":
    size = 100
    # arr = random.sample(range(size * 10), size)
    # reverse sorted array so we get the worst case
    # arr = list(range(size, 0, -1))
    # worst case is always
    arr = list(range(1, size))
    wanted_steps = size * math.log(size, 2)
    print(arr)
    print(f"wanted steps: {wanted_steps}")
    steps = merge_sort(arr)
    print(f"Steps taken: {steps}")
    print("Sorted array:", arr)
