from random import randint

A = [1,1,1,1,1,1,1,1,10]
total = 0

A.sort()

for x in range(0, (len(A)- 1)):
    total = total + A[x]

if A[len(A)- 1] > total:
    print ("False")

