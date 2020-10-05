# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = [0 for _ in range(elements)]
    k = 0
    j = 0
    for i in range(elements):
        if k > len(arrA):
            merged_arr[i] = arrB[j]
            j += 1
        elif j > len(arrB):
            merged_arr[i] = arrA[k]
            k += 1
        elif arrA[k] < arrB[j]:
            merged_arr[i] = arrA[k]
            k += 1
        else:
            merged_arr[i] = arrB[j]
            j += 1
    # while i < elements and j < elements:
    #     if arrA[i] < arrB[j]:
    #         merged_arr += arrA[i]
    #     else:
    #         merged_arr += arrB[j]
    #
    #     if i < len(arrA):
    #         merged_arr += arrB[i]
    #
    #     elif j < len(arrB):
    #         merged_arr += arrB[j]

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
        # mid = len(arr) // 2  # Finding the mid of the array
        # L = arr[:mid]  # Dividing the array elements
        # R = arr[mid:]  # into 2 halves
        #
        # merge_sort(L)  # Sorting the first half
        # merge_sort(R)  # Sorting the second half
        #
        # arr = merge(L, R)  # Combining the sorted halves storing in arr

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
