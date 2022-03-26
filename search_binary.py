import time
import random


def binary_search(array, target):
    left = 0
    right = len(array)-1
    i = 0
    while(left<=right):
        
        mid = int(round((left+right)/2, 0))
        #print(f'{i}, left={left}   right={right}   mid={mid}')
        
        if target==array[mid]:
            return mid
            
        elif target>array[mid]:
            left = mid+1
            
        elif target<array[mid]:
            right = mid
    
    return -999


def linear_search(array, target):
    for i in range(len(array)):
        if target==array[i]:
            return i

    return -999


if __name__ == "__main__":
    
    start_time = time.time()
    array_= [i for i in range(10000000)]
    target_ = 9999999
    
    #array_= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #target_ = 0
    
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