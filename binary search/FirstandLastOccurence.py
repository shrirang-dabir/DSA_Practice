#Q. FIND THE FIRST AND LAST OCCURRENCE OF A GIVEN ELEMENT IN A SORTED ARRAY
#BRUTE - O(N) - LINEAR SEARCH
#first = -1, last = -1. Traverse through the array and if x is found and first is -1, set first to current index. Keep updating last to current index if x is found.
def firstAndLastOccurrenceBrute (arr, x):
    first = -1
    last = -1
    n = len(arr)
    for i in range (n):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return (first, last)

#example usage:
arr = [2,4,6,8,8,8,11,13]
x = 8
print(f"Brute Force: First and Last Occurrence of {x} is: {firstAndLastOccurrenceBrute(arr, x)}")

#OPTIMIZED - O(logN) - BINARY SEARCH - USE LOWER BOUND AND UPPER BOUND
#lower bound = first occurance, last occurance = upper bound - 1
#edge case: if there is an element in the array, lower bound will be equal to upper bound, hence return -1 for both first and last occurrence
def lowerBound(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n # Initialize ans to n, which is out of bounds for the array
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1 #trim the right half as we want the smallest element >= x
        else:
            low = mid + 1
    return ans

def upperBound (arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n # Initialize ans to n, which is out of bounds for the array
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1 #trim the right half as we want the smallest element >= x
        else:
            low = mid + 1
    return ans

def firstAndLastOccurrenceOptimized (arr, x):
    n = len(arr)
    lb = lowerBound (arr, x)
    ub = upperBound (arr, x)
    if lb == n or arr[lb] != x: # If lower bound is out of bounds or the element at lower bound is not equal to x, it means x is not present in the array
        return (-1,-1)
    return (lb, ub - 1) #else return the lower bound and upper bound - 1 as the first and last occurrence respectively

# Example usage:
arr = [2,4,6,8,8,8,11,13]
x = 14
print(f"Optimized: First and Last Occurrence of {x} is: {firstAndLastOccurrenceOptimized(arr, x)}")

#USE PLAIN BINARY SEARCH TO FIND FIRST AND LAST OCCURRENCE
def firstOccurrence (arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first = mid #update first to current index of mid as we found it
            high = mid - 1 #we have to find forst occurrence i.e smallest index so search in left and trim right
        elif arr[mid] < x: #As mid is < x search in right half and trim left
            low = mid + 1
        else: #if mid > x, search in left half and trim right
            high = mid - 1
    return first

def lastOccurrence (arr, x):
    n = len (arr)
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1 #As we want last (largest index) occurrence, search in right part and trim left
        elif arr[mid] < x: #As mid < x, search in right half and trim left
            low = mid + 1
        else: #if mid > x, search in left half and trim right
            high = mid - 1
    return last

def firstAndLastOccurrenceBinarySearch(arr, x):
    f = firstOccurrence(arr, x)
    if f == -1: # If first occurrence is -1, it means x is not present in the array so first and last = (-1,-1)
        return (-1,-1)
    l = lastOccurrence(arr, x)
    return (f,l)

# Example usage:
arr = [2,8,8,8,8,8,11,13]
x = 10
print(f"Binary Search: First and Last Occurrence of {x} is: {firstAndLastOccurrenceBinarySearch(arr, x)}")

#Q. FIND TOTAL OCCURRENCES OF A GIVEN ELEMENT IN A SORTED ARRAY = LAST - FIRST + 1
def totalOccurrences(arr, x):
    f = firstOccurrence(arr, x)
    if f == -1:
        return 0 #element not present
    l = lastOccurrence(arr, x)
    return l - f + 1 
# Example usage:
arr = [2,8,8,8,8,8,11,13]
x = 8
print(f"Total Occurrences of {x} is: {totalOccurrences(arr, x)}")

