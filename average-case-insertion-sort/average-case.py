# CSC 382
# Dennis Krupitsky
# Project #3 Average Case - Insertion Sort
# Date: 3/5/20

# import lib
import random


# insertion sort method
def Insertion_Mod(A, n):
    global steps
    # set steps to 0
    steps = 0
    # bring in our global var for steps
    for i in range(1,n):
        j = i
        # increment count by 1 because there is always at least 1 comp
        steps += 1
        # inner loop to see if current value is greater than those ahead of it
        while A[j] < A[j-1] and j > 0: # ran into issue of out of index so i added check of j being > 0
            # increment steps
            steps += 1
            #sort the values
            temp = A[j]
            A[j] = A[j-1]
            A[j-1]=temp   
            j -=1 
    return A


    
# ------------------------------------ driver -------------------------------------------
# variables used
n = [100, 500, 1000, 2500, 3000, 3500]

bound = 3500
steps = 0









# output results
print ('Input Size'.ljust(35),'Calculated Average'.ljust(40), 'Real Average'.ljust(30))
print('-------------------------------------------------------------------------------------------------')
for input_size in n:
    # calculate average case
    calculatedAverage = ((pow(input_size,2) + input_size)/4) + (input_size/2)
    # reset real average
    tot_number_steps = 0
    # inner loop for 100000 times for real average
    for x in range(pow(10,5)):
        # generate list of random numbers
        A = random.sample(range(-bound, bound), input_size)
        # call sort method
        Insertion_Mod(A, input_size)
        tot_number_steps += steps
    # calculate real average
    realAverage = tot_number_steps / 100000

    #output
    print(str(input_size).ljust(30), str(calculatedAverage).center(25), ' '.ljust(4),  str(realAverage).center(43))

