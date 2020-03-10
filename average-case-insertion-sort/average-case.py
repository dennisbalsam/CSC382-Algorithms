# CSC 382
# Dennis Krupitsky
# Project #3 Average Case - Insertion Sort
# Date: 3/5/20

# import lib
import random

# variables used
A = []
n = 100
steps = 0
bound = 50

# insertion sort method
def Insertion_Mod(A, n):
    # bring in our global var for steps
    global steps

    for i in range(1,n):
        j = i
        while A[j] < A[j-1]:
            # increment steps based on comparisons
            steps += 1
            # print('comparing ', A[j], ' with ', A[j-1])

            #sort the values
            temp = A[j]
            A[j] = A[j-1]
            A[j-1]=temp
            j-=1    
    return A


    


A = random.sample(range(-bound, bound), n)


print(A)
# print(Insertion(Apru,len(A)))
# print(steps)

