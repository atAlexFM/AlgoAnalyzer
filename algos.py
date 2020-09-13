"""
    Defines all the algorithms to be tested.
    Quicksort, mergesort, bubblesort, and default Python sort algo
"""
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smallest, equal, largest = [], [], []
        for num in arr:
            if num < pivot:
                smallest.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                largest.append(num)
        return quicksort(smallest) + equal + quicksort(largest)

def merge_sorting(arr1, arr2):
    # Initialize a list
    sorted_arr = []

    # Branching and conditionals
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i +=1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def mergesort(arr):
    # Define base case
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2 # Divide by 2 as int
        list1 = mergesort(arr[:middle]) # Performs recurssion
        list2 = mergesort(arr[middle:])
        return merge_sorting(list1, list2)

def bubblesort(arr):
    swap = True
    while swap:
        swap = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

def pysort(arr):
    arr = []
    return sorted(arr)