# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0
    while arrA[i] < len(elements) and arrB[j] < len(elements):
        if arrA[i] < arrB[j]:
            merged_arr += arrA[i]
        else:
            merged_arr += arrB[j]

        if i < len(arrA):
            merged_arr += arrB[i]

        elif j < len(arrB):
            merged_arr += arrB[j]

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


def merge_sort_in_place(arr, l, r):
    # Your code here

