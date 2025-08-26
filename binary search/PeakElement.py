#Q. FIND PEAK ELEMENT IN AN ARRAY. ASSUME -INF AT BOTH ENDS. RETURN INDEX OF ANY PEAK ELEMENT
#PEAK ELEMENT IS AN ELEMENT WHICH IS GREATER THAN ITS NEIGHBORS - ARR[MID] > ARR[MID - 1] AND ARR[MID] > ARR[MID + 1]

#brute force: O(N)- TC, SC= O(1)
#traverse through array linearly and check for each element if it is greater than its neighbors
def findPeakBrute (arr):
    n = len(arr)
    if n == 1: #if only one element, it is the peak as array has -inf at both ends
        return arr[0]
    for i in range (n):
        #if it's the first element
        if ((i == 0) or (arr[i - 1] < arr[i])) and ((i == n - 1) or (arr[i] > arr[i + 1])):
            return i #return index of peak element
    return None  # If no peak element is found
# Example usage:
arr = [1,2,3,4,5,6,7,8,5,1]
print(f"Peak element in array is at index: {findPeakBrute(arr)}")

#optimal: O(log N) - TC, SC = O(1)
#step 1: check edge cases for single element and first and last elements. And trim search space
#step 2: check if mid is greater than its neighbors, then it is the peak
#step 3: check if mid is on increasing curve, peak is on right half, so eliminate left half: low = mid + 1
#step 4: if mid is on decreasing curve, peak is on left half, so eliminate right half: high = mid - 1
#step 5: for multiple peaks, if mid is at reverse of peak i.e on V shape, then we can choose either left or right half to continue searching for peak

def findPeakOptimal(arr):
    n = len(arr)
    #step 1: check edge cases
    if n == 1: #if only one element, it is the peak as array has -inf at both ends
        return 0
    if arr[0] > arr[1]: #if first element is greater than second, it is the peak
        return 0
    if arr[n-1] > arr[n - 2]: #if last element is greater than second last, it is the peak
        return n - 1
    #now, as first and last elements are checked, we exclude them and can proceed with binary search
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        #step 2: check if mid is greater than its neighbors, if yes it's the peak
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid - 1]: #step 3: peak is on increasing curve, so eliminate left half
            low = mid + 1
        elif arr[mid] < arr[mid + 1]: #step 4: peak is on decreasing curve, so eliminate right half
            high = mid - 1
        else: #step 5: mid is at reverse of peak i.e on V shape, we can choose either left or right half to continue searching for peak
            high = mid - 1 #or low = mid + 1, both will work
    return None  # If no peak element is found
# Example usage:
arr = [1,5,1,2,1]
print(f"Peak element in array is at index: {findPeakOptimal(arr)}")
