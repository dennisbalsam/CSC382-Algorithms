import time
import random

#This is a program that compares the execution time of Insertion Sort, Merge Sort, and Heap Sort for inputs of different size.

# insertion sort method
def insertionSort(A):
    # get len of n
    n = len(A)
    for i in range(1,n):
        j = i
        # inner loop to see if current value is greater than those ahead of it
        while A[j] < A[j-1] and j > 0: # ran into issue of out of index so i added check of j being > 0
            #sort the values
            temp = A[j]
            A[j] = A[j-1]
            A[j-1]=temp   
            j -=1 


# merge sort method (used my own, not from lecture)
def mergeSort(myList):
    if len(myList) > 1:
        # find mid
        mid = len(myList) // 2
        # split list into 2 halves
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)


        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        # merge the 2 halves together
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

# heap sort methods ( once again used my own instead of lecture one)

# function to create a max heap

def max_heap(A, n, i):
    # Find largest among root and children
    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2 
 
    # check if left or right node are larger
    if l < n and A[i] < A[l]:
        largest = l
 
    if r < n and A[largest] < A[r]:
        largest = r
 
    # if root is not largest, swap with largest found value and continue buliding heap
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heap(A, n, largest)
 
def heapSort(A):
    n = len(A)
 
    # build max heap
    for i in range(n, -1, -1): # filling in reverse
        max_heap(A, n, i)
 
    
    for i in range(n-1, 0, -1):
        # swap
        A[i], A[0] = A[0], A[i]  
        
        #put highest value at root
        max_heap(A, i, 0)





#----------------- driver ----------------------------------
#create bound for range of numbers
bound = 500000

# varying input sizes
n = [10, 1000, 10000, 50000,100000, 200000]
# different sorts
sorts = [insertionSort,mergeSort, heapSort]



#output format
print('Time is in seconds')
print ('Input Size'.ljust(35),'Insertion Sort'.ljust(40), 'Merge Sort'.ljust(30), 'Heap Sort'.ljust(30))
print('-------------------------------------------------------------------------------------------------------------------------------------------')

# loop using the different sorts
for input_size in n:
    # map to store times
    # [0] is insertionSort, [1] is mergeSort, [2] is heapSort
    times = []
    for i in range(len(sorts)):
        # create the random array (it will be the same all 3 times of inner loop due to seed)
        random.seed(2)
        A = random.sample(range(-bound, bound), input_size)
        
        # mark start time
        timeStart = time.time()

        # call the different sorts
        sorts[i](A)

        # store time for that sort
        times.append((time.time() - timeStart))
    #output values 
    print (str(input_size).ljust(30), str(round(times[0], 3)).center(24), ' '.ljust(15), str(round(times[1], 3)).center(19), ' '.ljust(9), str(round(times[2], 3)).center(24))





    
    





