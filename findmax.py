'''

AUTHOR : MICHAEL WOMACK
COURSE: CSCI 6212
PROFESSOR: Amrider Arora

'''

import sys
import numpy as np
import time


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def quick_sort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


def check_arr(arr,n):
    for i in range(1, n-1):
        if arr[i-1] > arr[i]:
            return False
    return True


def circular_shift(arr, n):
    result = quick_sort(arr, 0, n-1)
    print('Max is ' + str(result[n-1]))
    step = int(n-100) 
    shifted = np.roll(result,step)
    return shifted


def findMax(arr,low,high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    
    if mid < high and arr[mid] > arr[mid+1]:
        return arr[mid]
    
    if mid > low and arr[mid] < arr[mid -1]:
        return arr[mid -1]
    
    if arr[low] <= arr[mid]:
        return findMax(arr, mid+1, high)
    
    return findMax(arr, low, mid -1)


def main():
    n_values = [100000,200000,300000,400000,500000]
    maxs = []
    results = []

    sys.setrecursionlimit(1000000)

    j = 1
    for n in n_values:
        rand = np.random.rand(n)
        arr = circular_shift(rand, n)

        t0 = time.time()
        maxs.append(findMax(arr, 0, n-1))
        t1 = time.time()
        results.append(t1-t0)
        j+=1

    for i in range(len(results)):
        print("Results for " + str(n_values[i]))
        print('Time: ' + str(results[i]))
        print('Max ' + str(maxs[i]))


try:
    if __name__ == '__main__':
        main()
except TimeoutError:
    print('System timed out :)')