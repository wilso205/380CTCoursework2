import time
from random import randint

A = []

for x in range(0, 1000):
    A.append(randint(0,100))

print (len(A))
A.sort()
result = 0
base = 0
total = 0
half = 0
Partitioned = False

def subset_sum(A, target):
    Partitions = [0] * (target + 1)
    Partitions[0] = 1
    Partitions_next = Partitions[:]
    for x in A:
        for y in range(x, (target + 1)):
            Partitions_next[y] = Partitions_next[y] + Partitions[y - x]
        Partitions = Partitions_next[:]

    return Partitions[target]

print ("Dynamic Programming")
print (" ")

start = time.time()

for x in range(0, len(A)):
    total = total + A[x]

half = total/2

if half == int(half):
    target = int(half)
    result =(subset_sum(A, target))

if result == 0:
    print ("False")
else:
    print ("True")

end = time.time()
print ("Time taken: ")
print (end - start)
