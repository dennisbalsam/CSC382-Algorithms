import time
import random 
# recursive fibonacci function
def FiboR(value):
    if value == 0 or value == 1:
        return value
    return (FiboR(value - 1) + FiboR(value - 2))


def FiboNR(value) :
    # first 2 values of fibonacci
    Fib = [0,1]
    # loop until value entered
    for i in range(2, value + 1):
        Fib.append(Fib[i-1] + Fib[i-2])
    return Fib[value]


# test fib - recusrive
print('recursive fibonacci: ',  FiboR(10))
print('non-recursive fibonacci: ',  FiboNR(10))


#format outputs
print ('Integer'.ljust(20),'FiboR (seconds)'.ljust(25), 'FiboNR (seconds)'.ljust(30), 'Fibo-value')
print('-'.ljust(95, '-'))\

#different values for testing
values = [1,5,10, 15,20,25,30,35,40,45,55,60]

for j in range(len(values)):

    # time for recursive method
    timeStart = time.time()
    fibval = FiboR(values[j])
    fibRtime = time.time() - timeStart

    # time for non-recursive
    timeStart = time.time() 
    fibval = FiboNR(values[j])
    fibNRtime = time.time() - timeStart

    #output values 
    print (str(values[j]).ljust(15), str(round(fibRtime, 3)).center(24), ' '.ljust(11), str(fibNRtime).ljust(18), str(fibval).center(24))

