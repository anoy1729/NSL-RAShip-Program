import numpy
n,m = map(int, input().strip().split(' '))
a = []
b = []
for i in range(n):
    a = list(map(int,  input().strip().split(' ')))
for i in range(n):
    b = list(map(int,  input().strip().split(' ')))
a = numpy.array(a)
b = numpy.array(b)

print(numpy.add(a, b))                        
print(numpy.subtract(a, b))    
print(numpy.multiply(a, b))     
print(numpy.floor_divide(a, b))                        
print(numpy.mod(a, b))                                 
print(numpy.power(a, b))
    
