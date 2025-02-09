def quicksort(A, p, r):
    steps = 0
    if p < r:
        q, s = partition(A, p, r)
        steps += s
        steps += quicksort(A, p, q - 1)
        steps += quicksort(A, q + 1, r)
    return steps


def partition(A, p, q):
    steps = 0
    x = A[p]
    i = p
    for j in range(p + 1, q + 1):
        steps += 2
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            steps += 1
    A[p], A[i] = A[i], A[p]
    steps += 1
    return i, steps


if __name__ == "__main__":
    size = 100
    # arr = random.sample(range(size * 10), size)
    arr = list(range(1, 101))
    wanted_steps = size**2
    # wanted_steps = size * math.log(size, 2)
    print(arr)
    print(f"wanted steps: {wanted_steps}")
    steps = quicksort(arr, 0, len(arr) - 1)
    print(f"Steps taken: {steps}")
    print("Sorted array:", arr)
