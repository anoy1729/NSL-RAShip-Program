cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    op = []
    for i in range(n):
        if(i==0 or i==1):
            op.append(i)
        else:
            op.append(op[i-1]+op[i-2])
    
    return op
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
