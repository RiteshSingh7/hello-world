# Average case Time complexity is O(n^2)
# Space complexity is O(1)
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        hole = i
        while hole > 0 and arr[hole-1] > key:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = key 

# Driver code to test above code
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])