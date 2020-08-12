# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    count = len(arrA) + len(arrB)
    # Your code here
    ai = 0
    bi = 0
    while len(merged_arr) < count:
        if ai >= len(arrA):
            merged_arr.append(arrB[bi])
            bi += 1
        elif bi >= len(arrB):
            merged_arr.append(arrA[ai])
            ai += 1
        elif arrA[ai] < arrB[bi]:
            merged_arr.append(arrA[ai])
            ai += 1
        elif arrA[ai] >= arrB[bi]:
            merged_arr.append(arrB[bi])
            bi += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
