## Dot and Cross Product module *BETA*

# -- input style: [[$$$$,I,J,K,$$$$]...] indexes 1,2,3

## DOT PRODUCT ##

vectors = [['vector_1', 2,3,4,'test vector number 1 ...'],['vector_2',67,3,45,'test vector 2 of 2']]

import time

newvector = []
newvector.append("Vector_"+time.strftime("%m/%d/%Y"))
for x in range (1,4):
    newvector.append(vectors[0][x] * vectors[1][x])

print (newvector)
#return newvector
 
