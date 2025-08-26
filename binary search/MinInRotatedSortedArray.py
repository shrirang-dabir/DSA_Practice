#Q. FIND MIN ELEMENT IN A ROTATED SORTED ARRAY
#LINEAR SEARCH IS O(N) AND BINARY SEARCH IS O(LOGN)
#STEP1 - FIND MID AND DETERMINE WHICH HALF IS SORTED. INTRODUCE ANS VARIABLE AND STORE INF IN IT
#STEP2 - IF LEFT HALF IS SORTED, THEN MINIMUM ELEMENT IS IN RIGHT HALF. SO PICK UP MIN FROM LEFT HALF, COMPARE IT WITH ANS AND UPDATE ANS IF MIN IS LESS THAN ANS.
#THEN ELIMINATE THE LEFT HALF: LOW = MID + 1
#IF RIGHT HALF IS SORTED, THEN MINIMUM ELEMENT IS IN LEFT HALF. #SO PICK UP MIN FROM RIGHT HALF, COMPARE IT WITH ANS AND UPDATE ANS IF MIN IS LESS THAN ANS.
#THEN ELIMINATE THE RIGHT HALF: HIGH = MID - 1

def findMinInRotatedSorted(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf") # Initialize ans to infinity
    while low <= high:
        mid = (low + high) // 2
        #determine which half is sorted
        #if left is sorted
        if arr[low] <= arr[mid]:
            #pick up min from left half
            ans = min(ans, arr[low]) #min of left half is arr[low] as array is sorted
            #eliminate left half
            low = mid + 1
        #if right is sorted
        else:
            #pick up emin from right half
            ans = min(ans, arr[mid]) #min of right half is arr[mid] as array is sorted
            #eliminate right half
            high = mid - 1
    return ans  # Return the minimum element found
# Example usage:
arr = [7,8,9,1,2,3,4,5,6]
print(f"Minimum element in the rotated sorted array is: {findMinInRotatedSorted(arr)}") 

#FURTHER OPTIMIZED: IF SEARCH SPACE IS SORTED, THEN RETURN THE FIRST ELEMENT = arr[low]
#happenns when arr[low] <= arr[mid] and arr[mid] <= arr[high] i.e arr[low] <= arr[high]
def findMinInRotatedSortedOptimized(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")
    while low <= high:
        mid = (low + high) // 2
        #if search space is sorted, return the min of ans and first elemennt = arr[low]
        #occurs when it crosses the pivot point and the search space is sorted
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break # No need to continue searching, as the array is sorted
        #determine which half is sorted
        #if left is sorted
        if arr[low] <= arr[mid]:
            #pick up min from left half
            ans = min(ans, arr[low]) #min of left half is arr[low] as array is sorted
            #eliminate left half
            low = mid + 1
        #if right is sorted
        else:
            #pick up min from right half
            ans = min(ans, arr[mid])
            #eliminate right half
            high = mid - 1
    return ans  # Return the minimum element found
# Example usage:
arr = [4,5,6,0,1,2]
print(f"Optimized Minimum element in the rotated sorted array is: {findMinInRotatedSortedOptimized(arr)}")

#Q. FIND HOW MANY TIMES THE ARRAY IS ROTATED
#IF ARRAY IS SORTED, THEN IT IS ROTATED 0 TIMES
#NO. OF TIMES ROTATED = INDEX OF MINIMUM ELEMENT
def findRotationCount(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")
    rotation_count = 0
    while low <= high:
        mid = (low + high)//2
        #if search space is sorted, arr[low] is the minimum element
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                rotation_count = low
                ans = arr[low]
            break # No need to continue searching, as the array is sorted
        #determine which half is sorted
        #if left is sorted
        if arr[low] <= arr[mid]:
            #pick up min from left half
            if arr[low] < ans:
                rotation_count = low
                ans = arr[low]
            #eliminate left half
            low = mid + 1
        #if right is sorted
        else:
            #eliminate right half
            high = mid - 1
            if arr[mid] < ans:
                rotation_count = mid
                ans = arr[mid]
    return rotation_count  # Return the number of rotations
# Example usage:
arr = [3,4,5,1,2]
print(f"Array is rotated {findRotationCount(arr)} times.")
            
