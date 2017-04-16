#size = input("Enter the size of an array : ")
#array = [0 for x in range(size)]
from __future__ import division
array = [-4,3,-9,0,4,1]

positive = 0
zero = 0
negative = 0
length = len(array)
for i in range(0,length):
    if array[i] < 0 :
        negative += 1
    if array[i] == 0 :
        zero +=1
    if array[i] > 0 :
        positive +=1

print "The fractions are %.6f , %.6f, %.6f " %(negative/length, zero/length, positive/length)
