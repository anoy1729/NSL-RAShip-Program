import numpy
n,m = map(int, input().strip().split(' '))
a = numpy.array([input().split()for i in range(n)], int)
b = numpy.array([input().split()for i in range(n)], int)



print(numpy.add(a, b))                        
print(numpy.subtract(a, b))    
print(numpy.multiply(a, b))     
print(numpy.floor_divide(a, b))                        
print(numpy.mod(a, b))                                 
print(numpy.power(a, b))
    
