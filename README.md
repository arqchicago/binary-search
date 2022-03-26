# Binary Search
This technique finds the position of a value in an array that has already been sorted. The input to the algorithm is an array and a 
target value.

## Algorithm
The function assumes that the input array is already sorted. It starts by pointing to the first and last element of the array and reading
their index values (0, length(array)-1) into 'left' and 'right' variables. The left and right variables are then used to calculate the
middle value index. The algorithm compares this middle value to the target and if it is the same, it returns the index. Otherwise,
it compares if the target is greater than or less than the middle value. Depending on this comparison, the target value is either in 
the lower or upper half of the array. If, for example, the target value is greater than the middle value of the array, then the 'left' 
variable is updated to be the index of middle value. The middle index is calculated again and the process is repeated until either the 
target is found or the target is deemed to not be in the array. 

## Pseudocode
The pseudocode implemented is as follows:
'''
function binary_search(array, target):
    left = 0
    right = len(array)-1
    i = 0
    while(left<=right):
        
        mid = int(round((left+right)/2, 0))
        
        if target==array[mid]:
            return mid
            
        elif target>array[mid]:
            left = mid+1
            
        elif target<array[mid]:
            right = mid-1
    
    return -999
'''
