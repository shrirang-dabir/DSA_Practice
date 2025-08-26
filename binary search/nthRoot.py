#Q. FIND NTH ROOT OF A NUMBER NUM
#BRUTE FORCE APPROACH: TRAVERSE THROUGH ALL INTEGERS FROM 0 TO NUM AND CHECK IF RAISING IT TO THE POWER N IS EQUAL TO NUM
#TIME COMPLEXITY: O(NUM * LOG N)

def power (i, n):
    return i ** n

def nthroot (num, n):
    for i in range (num + 1):
        if power (i, n) == num:
            return i
        elif power (i, n) > num:
            break
    return None  # If no nth root is found
# Example usage of power function
print(f"Power of 2 raised to 3 is: {power(2, 3)}")  # Output: 8
# Example usage of nthroot function
num = 27
n = 3
print(f"The {n}th root of {num} is: {nthroot(num, n)}")  # Output: 3

#OPTIMAL APPROACH: USE BINARY SEARCH
#WRITE A FUNNCTION TO CALCULATE MID ^ N
#return 1 if mid ^ n == num, return 2 if mid ^ n > num (overflow case), return 0 if mid ^ n < num (continue searching)
#TC = O(n * log num)
def func (mid, n ,num):
    ans = 1
    for i in range (n):
        ans = ans * mid
        if ans > num:
            return 2 # If ans exceeds num, return 2: overflow case
    if ans == num:
        return 1 # If ans is equal to num, return 1: found nth root
    return 0 # If ans is less than num, return 0: continue searching

def nthrootOptimal (n, num):
    low = 1
    high = num
    while low <= high:
        mid = (low + high) // 2
        midN = func (mid, n, num)
        if midN == 1: # If mid^n is equal to num, return mid
            return mid
        elif midN == 0: #if mid^n is < num, eliminate left half and continue searching in right half
            low = mid + 1
        else: #if mid^n is > num, eliminate right half and continue searching in left half
            high = mid - 1
    return None  # If no nth root is found
# Example usage of nthrootOptimal function
num = 69
n = 3
print(f"The {n}th root of {num} using optimal approach is: {nthrootOptimal(n, num)}")  # Output: 4
