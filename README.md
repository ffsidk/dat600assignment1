# Assignment 1 DAT600 Group 15

DAT600 Algorithm Theory Assignment 1 for group 15.

## Task 1 counting the steps

### Python

The python directory contains code for Task 1 (and task 2) where we implement and count the steps of sorting algorithms.
There are two dependencies: matplotlib (for plotting) and pyqt6 (for displaying the plot output in linux).

Only the "main.py" file is required to get the output plot, but all the separate python files have their own respective test code for each sorting algorithm.

The python lists chosen to sort has been initialized to be the worst-case of each sorting algorithm in order to get a deterministic and accurate number of steps. This was done to be able to compare the actual step count to the desired step count. The output is not perfect but it is pretty accurate and deterministic.

To run the code in this directory execute the following commands:

```bash
cd python
pip3 install -r requirements.txt
python3 main.py
```

## Task 2

### Python

Along with code for task 1, the python directory also contains python file for task 2. This python script uses a performance counter to get the execution time with inputs of varying sizes.

To run the insertion sort timer script run the following:

```bash
cd python
python3 timeinsertionsort.py
```

### Go

The go directory contains code belonging to task 2. This go code times the execution of insertion sort for the same varying input sizes as the python script above.

To run the code in this directory execute the following commands:

```bash
cd go
go run main.go
```
