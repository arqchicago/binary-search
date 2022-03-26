import time
import random


def binary_search(array, target):
    '''
    binary_search function performs binary search to find a target in a sorted array
    
    
    :param array:   a python list containing elements
    :param target:  a target value to be found in the array
    
    :return:        index of target if the target is found in the array, otherwise -999
    '''
    
    left = 0
    right = len(array)-1
    i = 0
    while(left<=right):
        
        # caculate middle index of the array
        mid = int(round((left+right)/2, 0))
        
        # if target equals middle value of the array, return items
        # otheriwse, update left or right variables based on which half the target may be contained in
        if target==array[mid]:
            return mid
            
        elif target>array[mid]:
            left = mid+1
            
        elif target<array[mid]:
            right = mid-1
    
    return -999


def linear_search(array, target):
    '''
    linear_search function performs linear search to find a target in a sorted array
    
    
    :param array:   a python list containing elements
    :param target:  a target value to be found in the array
    
    :return:        index of target if the target is found in the array, otherwise -999
    '''

    # simply iterate over all elements of the array and compare against the target
    for i in range(len(array)):
        if target==array[i]:
            return i

    return -999


if __name__ == "__main__":
    
    start_time = time.time()
    array_= [i for i in range(200000000)]
    target_ = 199999999
    
    #array_= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #target_ = 2
    
    print(f'array created:  array length={len(array_)},  target={target_},  time={time.time()-start_time}')

    start_time = time.time()
    idx = linear_search(array_, target_)

    
    if idx != -999:
        print(f'linear search:  index={idx},  value={array_[idx]},  target={target_},  time={time.time()-start_time}')
    
    else:
        print(f'linear search:  index={idx},  value=NOT FOUND,  target={target_},  time={time.time()-start_time}')

    start_time = time.time()
    idx = binary_search(array_, target_)

    
    if idx != -999:
        print(f'binary search:  index={idx},  value={array_[idx]},  target={target_},  time={time.time()-start_time}')
    
    else:
        print(f'binary search:  index={idx},  value=NOT FOUND,  target={target_},  time={time.time()-start_time}')