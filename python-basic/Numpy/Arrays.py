import numpy

def arrays(arr):
    nmbr = []
    for i in range(len(arr)):
        nmbr.append(float(arr[i]))
    np = numpy.array(nmbr)
    np = numpy.flip(np)
    return np
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
