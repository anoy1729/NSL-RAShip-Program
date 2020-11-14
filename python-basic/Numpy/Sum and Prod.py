import numpy
n,m = map(int, input().strip().split(' '))
a = []
for i in range(n):
    a.append(list(map(int, input().strip().split(' '))))
    
a = numpy.array(a)
b = (numpy.sum(a, axis = 0))

print(numpy.prod(b))
