import matplotlib.pyplot as plt
import quicksort
import heapsort
import insertionsort
import mergesort
import math
import sys

sys.setrecursionlimit(10**6)

sizes = [10, 50, 100, 500, 1000]
insert_steps, merge_steps, heap_steps, quick_steps = [], [], [], []


# WANTED sort steps:
wanted_insertion_sort_steps = [n**2 for n in sizes]
wanted_merge_sort_steps = [n * math.log(n, 2) for n in sizes]
wanted_heap_sort_steps = [n * math.log(n, 2) for n in sizes]
wanted_quick_sort_steps = [n**2 for n in sizes]

# print(f"Wanted insertion steps: {wanted_insertion_sort_steps}")
# print(f"Wanted merge steps: {wanted_merge_sort_steps}")
# print(f"Wanted heap steps: {wanted_merge_sort_steps}")
# print(f"Wanted quick steps: {wanted_quick_sort_steps}")

# for size in sizes:
for idx, size in enumerate(sizes):
    print(f"Running size: {size}")
    # arr = random.sample(range(size * 10), size)
    # arr = [i for i in range(size - 1, -1, -1)]
    # Worst-case array for Insertion Sort (reverse-sorted array)
    insertion_worst = list(range(size, 0, -1))

    # Worst-case array for Heap Sort (already max-heapified array, but not sorted)
    heap_worst = list(
        range(1, size + 1)
    )  # Heap sort's worst case is similar to its average case

    # Worst-case array for Merge Sort (array that maximizes the number of comparisons, typically already sorted)
    merge_worst = list(range(1, size + 1))

    # Worst-case array for Quick Sort (sorted or reverse-sorted array, depending on pivot choice)
    quick_worst = list(range(1, size + 1))  # Assuming pivot is first element

    # quicksort_sorted, quicksort_steps = quicksort.quicksort(arr.copy(), 0, len(arr) - 1)
    quicksort_steps = quicksort.quicksort(quick_worst, 0, len(quick_worst) - 1)
    print(f"Quicksort steps: {quicksort_steps}")
    print(f"Desired (precalculated) quicksort steps: {wanted_quick_sort_steps[idx]}")
    quick_steps.append(quicksort_steps)

    # heapsort_sorted, heapsort_steps = heapsort.heap_sort(arr.copy())
    heapsort_steps = heapsort.heap_sort(heap_worst)
    print(f"Heapsort steps: {heapsort_steps}")
    print(f"Desired (precalculated) heapsort steps: {wanted_heap_sort_steps[idx]}")
    heap_steps.append(heapsort_steps)

    # insertion_sorted, insertion_steps = insertionsort.insertion_sort(arr.copy())
    insertion_steps = insertionsort.insertion_sort(insertion_worst)
    print(f"Insertionsort steps: {insertion_steps}")
    print(
        f"Desired (precalculated) insertionsort steps: {wanted_insertion_sort_steps[idx]}"
    )
    insert_steps.append(insertion_steps)

    # mergesort_sorted, mergesort_steps = mergesort.merge_sort(arr.copy())
    mergesort_steps = mergesort.merge_sort(merge_worst)
    print(f"Mergesort steps: {mergesort_steps}")
    print(f"Desired (precalculated) mergesort steps: {wanted_merge_sort_steps[idx]}")
    merge_steps.append(mergesort_steps)
    print()

fig = plt.figure(figsize=(14, 10))  # Adjust window size
plt.suptitle("Sorting Algorithm Analysis", y=0.98, fontsize=14)

ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2)  # Spans entire top row
ax1.plot(sizes, insert_steps, label="Insertion Sort (Θ(n²))", marker="o")
ax1.plot(sizes, merge_steps, label="Merge Sort (Θ(n log n))", marker="s")
ax1.plot(sizes, heap_steps, label="Heap Sort (O(n log n))", marker="^")
ax1.plot(sizes, quick_steps, label="Quicksort (Θ(n²))", marker="d")
ax1.set_title("All Algorithms Comparison")
ax1.set_xlabel("Input Size (n)")
ax1.set_ylabel("Number of Steps")
ax1.legend()
ax1.grid()


def plot_algorithm(ax, data, title, marker, position):
    ax.plot(sizes, data, label=title, marker=marker, color=plt.cm.tab10(position))
    ax.set_title(title.split("(")[0].strip())
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Steps")
    ax.grid()
    ax.legend()


ax2 = plt.subplot2grid((3, 2), (1, 0))
plot_algorithm(ax2, insert_steps, "Insertion Sort (Θ(n²))", "o", 0)

ax3 = plt.subplot2grid((3, 2), (1, 1))
plot_algorithm(ax3, merge_steps, "Merge Sort (Θ(n log n))", "s", 1)

ax4 = plt.subplot2grid((3, 2), (2, 0))
plot_algorithm(ax4, heap_steps, "Heap Sort (O(n log n))", "^", 2)

ax5 = plt.subplot2grid((3, 2), (2, 1))
plot_algorithm(ax5, quick_steps, "Quicksort ((Θ(n²))", "d", 3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
