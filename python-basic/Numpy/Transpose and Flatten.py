import numpy
n , m = map(int, input().strip().split(' '))
a = []
for i in range(n):
    a.append( list(map(int, input().strip().split(' '))) )
a = numpy.array(a)    
print(numpy.transpose(a))
print(a.flatten())
