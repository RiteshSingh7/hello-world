# Time complexity is O(n*logn)
# Space complexity is O(logn)
# Randomized Quick sort ( avoids worst case of O(n^2) time )
from random import randint

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = low              # index of smaller element 
    pivot = arr[high]    # pivot 

    for j in range(low , high): 
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot:        
            arr[i],arr[j] = arr[j],arr[i] 
            # increment index of smaller element 
            i = i+1

    arr[i],arr[high] = arr[high],arr[i] 
    return i

# This function chooses a random pivot and swaps with the last element
def randomized_partition(arr,low,high):
    p = randint(low,high)
    arr[p],arr[high] = arr[high],arr[p]
    return partition(arr,low,high)

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 

        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = randomized_partition(arr,low,high) 

        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])