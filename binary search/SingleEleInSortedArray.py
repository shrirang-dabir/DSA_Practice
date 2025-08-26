#Q. FIND SINGLE ELEMENT IN A SORTED ARRAY
#BRUTE FORCE APPROACH: TRAVERSE THROUGH THE ARRAY AND CHECK FOR EACH ELEMENT. IF IT IS NOT EQUAL TO ITS PREVIOUS OR NEXT ELEMENT, THEN IT IS THE SINGLE ELEMENT.
#TIME COMPLEXITY: O(N)
def findSingleElementBrute(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in range(n):
        #if it's the first element
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        #if it's the last element
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        #if it's in the middle
        else:
            if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
                return arr[i]
    return None  # If no single element is found
# Example usage:
arr = [1,1,2,2,3,3,4,5,5,6,6]
print(f"Single element in the sorted array is: {findSingleElementBrute(arr)}")

#OPTIMAL APPROACH: BINARY SEARCH
#TIME COMPLEXITY: O(log N)
#STEP 1: CHECK EDGE CASES FOR FIRST AND LAST ELEMENTS
#STEP 2: CHECK IF THE MID ELEMENT IS NOT EQUAL TO ITS NEIGHBORS, THEN IT IS THE SINGLE ELEMENT
#STEP 3; CHECK IF MID IS ON LEFT HALF: IF MID IS ON ODD INDEX AND PREVIOUS ELEMENT (ON EVEN INDEX) IS EQUAL TO MID AND IF MID IS ON EVEN AND NEXT ELEMENT (ON ODD INDEX) IS EQUAL TO MID
         #IF YES ELIMINATE LEFT HALF: LOW = MID + 1 AS SINGLE ELEMENT IS ON RIGHT HALF
#STEP4: IF MID IS ON RIGHT HALF, ELIMINATE RIGHT HALF AS SINGLE ELEMENT IS ON LEFT HALF: HIGH = MID - 1

def findSingleElementOptimal (arr):
    n = len(arr)
    #step 1: Check edge cases
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    #now, as first and last elements are checked, we exclude them and can proceed with binary search
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        #step 2: check if mid is equal to its neighbors
        if (arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]): 
            return arr[mid] #it is a single element
        #step 3: check if mid is on left half
        #if mid is odd and previous element is equal to mid or if mid is even and next element is equal to mid
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            low = mid + 1 #mid is on left half, so eliminate left half as our target single element is on right half
        #step 4: if mid is on right half, eliminate right half as single element is on left half
        else:
            high = mid - 1
    return None  # If no single element is found
# Example usage:
arr = [1,1,2,2,3,3,4,5,5,6,6]
print(f"Single element in the sorted array is: {findSingleElementOptimal(arr)}")


