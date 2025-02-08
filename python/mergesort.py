import math


# def merge_sort(A, a=0, b=None):
#     steps = 0
#     if b is None:
#         steps += 1
#         b = len(A)
#         steps += 1
#     if 1 < b - a:
#         steps += 1
#         c = (a + b + 1) // 2
#         steps += 1
#         steps += merge_sort(A, a, c)
#         steps += merge_sort(A, c, b)
#         L, R = A[a:c], A[c:b]  # not sure
#         # steps += len(A[a:c])
#         # steps += len(A[c:b])
#         steps += merge(L, R, A, len(L), len(R), a, b)
#     return steps
#
#
# def merge(L, R, A, i, j, a, b):
#     steps = 0
#     if a < b:
#         steps += 1
#         if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
#             steps += 1
#             A[b - 1] = L[i - 1]
#             steps += 1
#             i = i - 1
#             steps += 1
#         else:
#             steps += 1
#             A[b - 1] = R[j - 1]
#             steps += 1
#             j = j - 1
#             steps += 1
#         steps += merge(L, R, A, i, j, a, b - 1)
#     return steps


# def merge_sort(A, a=0, b=None):
#     steps = 0
#     if b is None:
#         b = len(A)
#         steps += 1  # Counting the initialization of `b`
#
#     if 1 < b - a:
#         c = (a + b + 1) // 2
#         steps += 1  # Counting the division operation
#
#         # Recursively sort the two halves
#         steps += merge_sort(A, a, c)
#         steps += merge_sort(A, c, b)
#
#         # Merge the two halves
#         L, R = A[a:c], A[c:b]
#         steps += merge(L, R, A, a, b)
#     return steps
#
#
# def merge(L, R, A, a, b):
#     steps = 0
#     i = j = 0
#     k = a
#
#     # Merge the two subarrays
#     while i < len(L) and j < len(R):
#         steps += 1  # Counting the comparison
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1
#         k += 1
#         steps += 1  # Counting the assignment
#
#     # Copy remaining elements of L (if any)
#     while i < len(L):
#         A[k] = L[i]
#         i += 1
#         k += 1
#         steps += 1  # Counting the assignment
#
#     # Copy remaining elements of R (if any)
#     while j < len(R):
#         A[k] = R[j]
#         j += 1
#         k += 1
#         steps += 1  # Counting the assignment
#
#     return steps


# def merge_sort(A, a=0, b=None):
#     steps = 0
#     if b is None:
#         b = len(A)
#         steps += 1  # Counting the initialization of `b`
#
#     if 1 < b - a:
#         c = (a + b + 1) // 2
#         steps += 1  # Counting the division operation
#
#         # Recursively sort the two halves
#         steps += merge_sort(A, a, c)
#         steps += merge_sort(A, c, b)
#
#         # Merge the two halves
#         L, R = A[a:c], A[c:b]
#         steps += merge(L, R, A, a, b)
#     return steps
#
#
# def merge(L, R, A, a, b):
#     steps = 0
#     i = j = 0
#     k = a
#
#     # Merge the two subarrays
#     while i < len(L) and j < len(R):
#         steps += 1  # Counting the comparison
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1
#         k += 1
#         # Do not count assignments separately; they are part of the comparison step
#
#     # Copy remaining elements of L (if any)
#     while i < len(L):
#         A[k] = L[i]
#         i += 1
#         k += 1
#         steps += 1  # Counting the assignment
#
#     # Copy remaining elements of R (if any)
#     while j < len(R):
#         A[k] = R[j]
#         j += 1
#         k += 1
#         steps += 1  # Counting the assignment
#
#     return steps
def merge_sort(A, a=0, b=None):
    steps = 0
    if b is None:
        b = len(A)
        # Do not count initialization of `b` as a step

    if 1 < b - a:
        c = (a + b + 1) // 2
        # Do not count the division operation as a step

        # Recursively sort the two halves
        steps += merge_sort(A, a, c)
        steps += merge_sort(A, c, b)

        # Merge the two halves
        L, R = A[a:c], A[c:b]
        steps += merge(L, R, A, a, b)
    return steps


def merge(L, R, A, a, b):
    steps = 0
    i = j = 0
    k = a

    # Merge the two subarrays
    while i < len(L) and j < len(R):
        steps += 1  # Count the comparison
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        # Do not count assignments separately; they are part of the comparison step

    # Copy remaining elements of L (if any)
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
        steps += 1  # Count the assignment

    # Copy remaining elements of R (if any)
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
        steps += 1  # Count the assignment

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
