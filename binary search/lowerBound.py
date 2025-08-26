
#Q. FIND LOWER BOUND OF A GIVEN ELEMENT IN A SORTED ARRAY
# A. The lower bound of a given element in a sorted array is ARR[i] >= x, where i is the smallest index such that AR[i] >= x.
#Q. SEARCH INSERTION POINT OF A GIVEN ELEMENT IN A SORTED ARRAY
# A. The insertion point is the index where the element can be inserted while maintaining the sorted order of the array.
# This is equivalent to finding the lower bound of the element in the sorted array.
def lowerBound(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n  # Initialize ans to n, which is out of bounds for the array
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x: #satisfy the condition. hence search to smallest in left
            ans = mid  # Update ans to the current mid index
            high = mid - 1 # Move to the left half
        else: # arr[mid] < x, hence search to right
            low = mid + 1
    return ans  # Return the index of the lower bound, or n if not found
# Example usage:
arr = [1,2,3,3,5,8,8,10,10,11]
x = 9
print(lowerBound(arr, x))  # Output: 7, which is the index of the first element >= 9

#Q. FIND UPPER BOUND OF A GIVEN ELEMENT IN A SORTED ARRAY
# A. The upper bound of a given element in a sorted array is ARR[i] > x, where i is the smallest index such that AR[i] > x.
def upperBound(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n # Initialize ans to n, which is out of bounds for the array
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1 # Move to the left half
        else:
            low = mid + 1
    return ans  # Return the index of the upper bound, or n if not found
# Example usage:
arr = [2,3,6,7,8,8,11,11,11,12]
x = 10
print(upperBound(arr, x))  # Output: 6, which is the index of the first element > 10
