import numpy as np

inp = list(map(int, input().split()))
arr = []

for i in range(inp[0]):
    inp2 = list(map(int, input().split()))
    arr.append(inp2)
    
nparr = np.array(arr)
np.set_printoptions(legacy='1.13') #discussion
print (np.mean(nparr, axis = 1)) 
print (np.var(nparr, axis = 0)) 
print (np.std(nparr, axis = None)) 
