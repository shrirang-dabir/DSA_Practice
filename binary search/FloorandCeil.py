#Q. FIND THE FLOOR AND CEIL OF A GIVEN ELEMENT IN A SORTED ARRAY
# A. The floor of a given element in a sorted array is the largest element that is less than or equal to the given element, and the ceil is the smallest element that is greater than or equal to the given element.
#CEIL = LOWER BOUND
def floor (arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    floor_val = -1 # Initialize floor_val to -1, which indicates no floor found
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            floor_val = arr[mid] # Update floor_val to the current mid value
            low = mid + 1 # Move to the right half as we want the largest element <= x
        else:
            high = mid - 1
    return floor_val  # Return the floor value, or -1 if not found

def ceil (arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ceil_val = n # Initialize ceil_val to n, which indicates no ceil found
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ceil_val = arr[mid]
            high = mid - 1 # Move to the left half as we want the smallest element >= x
        else:
            low = mid + 1
    return ceil_val  # Return the ceil value, or n if not found

# Example usage:
arr = [10, 20, 30, 40, 50]
x = 25
print (f"Floor of {x} is: {floor(arr, x)} and ceil is {ceil(arr,x)}")