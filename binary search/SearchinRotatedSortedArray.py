#Q. SEARCH FOR AN ELEMENNT IN A ROTATED SORTED ARRAY (UNIQUE ELEMENTS)
# A. A rotated sorted array is an array that has been rotated at some pivot point,
# meaning that the elements are in sorted order but have been shifted to the right or left.
#BRUTE FORCE APPROACH - LINEAR SEARCH - O(N)
def rotatedSortedSearchBrute (arr, target):
    n = len(arr)
    for i in range (n):
        if arr[i] == target:
            return i
    return -1  # If the target is not found, return -1
# Example usage:
arr = [7,8,9,1,2,3,4,5,6]
target = 1
print(f"Brute Force: Element {target} found at index: {rotatedSortedSearchBrute(arr, target)}")

#OPTIMIZED APPROACH - BINARY SEARCH - O(logN)
def rotatedSortedSearchOptimal(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        # Check if the mid element is the target
        if arr[mid] == target:
            return mid
        #determine which half is sorted
        #if left half is sorted
        if arr[low] <= arr[mid]:
            #check if target is in left half
            if arr[low] <= target and target <= arr[mid]:
                #if yes, trim the right half
                high = mid - 1
            else:
                #if no, trim the left half
                low = mid + 1
        #if right half is sorted
        else:
            #check if target is in right half
            if arr[mid] <= target and target <= arr[high]:
                #if yes, trim left half
                low = mid + 1
            else:
                #if no trim right half
                high = mid - 1
    return -1  # If the target is not found, return -1
# Example usage:
arr = [7,8,9,1,2,3,4,5,6]
target = 1
print(f"Optimal: Element {target} found at index: {rotatedSortedSearchOptimal(arr, target)}")

#Q. SEARCH FOR AN ELEMENNT IN A ROTATED SORTED ARRAY (DUPLICATE ELEMENTS) RETURN TRUE IF FOUND, ELSE FALSE
#Here, we can use the same approach as above, but we need to handle the case where there are duplicate elements.
#case is when arr[low] == arr[mid] == arr[high], we cannot determine which half is sorted, so we can simply trim the search space by incrementing low and decrementing high to skip the duplicates
def rotatedSortedSearchDuplicates(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        #check if mid element is target
        if arr[mid] == target:
            return True
        #check our case of duplicates
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue # If we cannot determine which half is sorted, we skip the duplicates
        #determine which half is sorted
        #if left half is sorted
        if arr[low] <= arr[mid]:
            #check if target is in left half
            if arr[low] <= target and target <= arr[mid]:
                #if yes, trim the right half
                high = mid - 1
            else:
                #if no, trim the left half
                low = mid + 1
        #if right half is sorted
        else:
            #check if target is inn right half
            if arr[mid] <= target and target <= arr[high]:
                #if yes, trim left half
                low = mid + 1
            else:
                #if no trim right half
                high = mid - 1
    return False  # If the target is not found, return False
# Example usage:
arr = [3,1,2,3,3,3,3]
target = 1
print(f"Element {target} found: {rotatedSortedSearchDuplicates(arr, target)}")  # Output: True        