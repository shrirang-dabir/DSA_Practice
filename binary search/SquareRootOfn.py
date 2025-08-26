#Q. FIND THE SQUARE ROOT OF A NUMBER NUM. IF NUM IS NOT A PERFECT SQUARE, RETURN THE FLOOR VALUE OF THE SQUARE ROOT
#RETURN THE LARGEST INTEGER N SUCH THAT SQUARING IT DOES NOT EXCEED THE GIVEN NUMBER NUM

#brute force: TC = O(N), SC = O(1)
#traverse through all integers from 0 to num and check if squaring it is less than or equal to num
def squareRootBrute(num):
    if num < 0:
        return None
    for i in range (num  + 1):
        if i * i > num:
            return i - 1
    return num  # If num is 0 or 1, return num itself as its square root
# Example usage:
num = 16
print(f"Square root of {num} using brute force is: {squareRootBrute(num)}")

#optimal: use binary search
#TC = O(log N), SC = O(1)
#step 1: check edge cases for 0 and 1
#step 2: set low = 1 and high = num
#step 3: while low <= high, calculate mid = (low + high) // 2
#step 4: if mid * mid == num, return mid
#step 5: if mid * mid < num, then square root is on right half
#step 6: if mid * mid > num, then square root is on left half
def squareRootOptimal (num):
    if num < 0:
        return None
    if num == 0 or num == 1:
        return num
    low = 1
    high = num
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == num:
            return mid
        elif mid * mid < num: #if mid * mid is less than num, sq rt is on right half so eliminate left half
            low = mid + 1
        else:
            high = mid - 1
    return high  # Return the floor value of the square root. After low crosses high, high will be the largest integer whose square is less than or equal to num
# Example usage:
num = 20
print(f"Square root of {num} using optimal approach is: {squareRootOptimal(num)}")

