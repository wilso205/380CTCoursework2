import time
from random import randint

A = []

Set1 = 0
Set2 = 0
total = 0

for x in range(0, 1000000):
    A.append(randint(0,10))

beginning = time.time()

A.sort()
start = len(A) - 1

for x in range(0, len(A)):
    total = total + A[x]

if total % 2 == 0:
    for x in range(start, -1, -1):
        if Set1 > Set2:
            Set2 = Set2 + A[x]
        else:
            Set1 = Set1 + A[x]
else:
    Set1 = 1

if Set1 == Set2:
    print ("True")
else:
    print ("False")

end = time.time()
print ("Time taken: ")
print (end - beginning)
