import numpy
n,m,p = map(int, input().strip().split(' '))

a = []
b = []
for i in range(n):
    arr = list(map(int, input().strip().split(' ')))
    a.append(arr)
for i in range(m):
    arr = list(map(int, input().strip().split(' ')))
    b.append(arr)

a = numpy.array(a)
b = numpy.array(b)

print(numpy.concatenate((a, b), axis = 0))
