# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    """
    this recursive call should bring us closer to reaching
    the base case(s)
    base case(s): when does the recursion stop?
    it stops when we either find the target
    or start and end go past each other(i.e. we didn't find the target)

    """
    if start > end:
        # target is not in the array
        return -1
    else:
        mid = (start + end) // 2

        if arr[mid] == target:
            # this is our second base
            return mid
        """
        otherwise, we need to move towards one of our base cases
        arr doesn't change, just because we'll end updating start and end
        target doesn't change between recursive calls
        end changes if we're tossing out the right side of the array
        
        """
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        # start changes if we're tossing out the left side of the array
        else:

            return binary_search(arr, target, mid + 1, end)




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

      pass