package main

import (
	"fmt"
	"time"
)

func insertionSort(arr []int) {
	var helper func([]int, int)
	helper = func(arr []int, i int) {
		if i > 0 {
			helper(arr, i-1)
			insertLast(arr, i)
		}
	}
	helper(arr, len(arr)-1)
}

func insertLast(arr []int, i int) {
	if i > 0 && arr[i] < arr[i-1] {
		arr[i], arr[i-1] = arr[i-1], arr[i]
		insertLast(arr, i-1)
	}
}

func main() {
	sizes := []int{10, 50, 100, 500, 1000, 10000, 20000}
	for _, size := range sizes {
		// Create reverse-sorted array
		arr := make([]int, size)
		for i := 0; i < size; i++ {
			arr[i] = size - i
		}

		start := time.Now()
		insertionSort(arr)
		duration := time.Since(start)

		fmt.Printf("Size: %d, Time taken: %v \n", size, duration)
	}
}
