# CSC 382
# Dennis Krupitsky
# Project #3 Average Case - Insertion Sort
# Date: 3/5/20

def Insertion(A, n):
    for i in range(1,n):
        j = i
        while A[j] < A[j-1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1]=temp
            j-=1    
    return A



A=[0,1,4,8,2,9,3,5]
print(Insertion(A,len(A)))

