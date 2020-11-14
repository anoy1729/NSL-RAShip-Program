import numpy

n,m = map(int, input().strip().split(' '))
a = []
for i in range(n):
    a.append(list(map(int, input().strip().split(' '))))
    
a = numpy.array(a)
b = numpy.min(a, axis = 1) 
print(numpy.max(b) )
