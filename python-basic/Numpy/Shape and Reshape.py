import numpy
arr = list(map(int, input().strip().split(' ')))
np = numpy.array(arr)
print(numpy.reshape(np,(3,3)))
