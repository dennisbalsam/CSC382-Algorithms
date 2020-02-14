# program that demonstartes the average case complexity of how quickly the average time increases when the size of n increases

import random


# find function which returns position or 0
def Find(x, A, n):
    for j in range(n):
        if(x == A[j]):
            return (j+1)
    return 0

# function that compares the calculated average and the real average
def avgcomparison(bound):
    # variables
    n = 50
    hits= 0 
    x = 27
    totalSteps = 0
    # create array and loop to fill it with sub-sequences (going to be 10000 * 50 2Darray)
    sequence = []
    
    # loop 10000 times
    for i in range(10**4):
            sequence.append([random.randint(0, bound) for x in range(50)])

    # using find function for calculated average and real average for each subsequence in sequence
    for subseq in sequence:
        search = Find(x, subseq, n)
        if search != 0:
            # increment hits for calculated average
            hits+=1
            # increment total steps for real average
            totalSteps += search
        else:
            #increment total steps by length of the subsequence
            totalSteps += len(subseq)

    # calculated average
    q = hits/10000
    calculatedAverage = round((n + (q/2) - ((q*n)/2)),4)
    
    # real average
    realAverage = totalSteps/10000

        #print values
    print(str(bound).ljust(20), str(calculatedAverage).center(25), ' '.ljust(4),  str(realAverage).center(24))




# execute function with different sizes of bounds
bound = [30, 50, 80, 100, 1000, 10000]
print ('Bound'.ljust(25),'Calculated Average'.ljust(30), 'Real Average'.ljust(30))

# calulcated different averages as bound increases
for value in bound:
    avgcomparison(value)