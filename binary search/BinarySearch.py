
def binarySearch (arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#example usage
arr = [3,4,6,7,9,12,16,17]
target = 6
result = binarySearch(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")

#Recursive Binary Search
def binarySearchRecursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearchRecursive(arr, mid + 1, high, target) #low = mid + 1
    else:
        return binarySearchRecursive(arr, low, mid - 1, target)
#example usage
arr = [3,4,6,7,9,12,16,17]
target = 6
result = binarySearchRecursive(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")