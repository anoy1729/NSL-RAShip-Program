def print_rangoli(size):
    total = (n*2)-1
    maxm = (n-1)*4+1
    left=right = (maxm -1)//2
    rev = [] 
    for x in range(1,total+1,2):
        lchar = ''
        rchar = ''
        mchar = ''
        final = ''
        cval = 96+n

        for l in range(left):
            lchar = lchar + '-'


        for m in range((2*x)-1): # x = 5 , e-d-c-d-e , range = 9, mid = 5
            mid = ((2*x)-1)//2 
            if(m%2!=0):
                mchar = mchar + '-'
            elif(m<mid):
                mchar = mchar + chr(cval)
                cval = cval-1
            
            elif(m>=mid):
                mchar = mchar + chr(cval)
                cval = cval+1

        for r in range(right):
            rchar = rchar + '-'
        left = left-2
        right = right-2
        final = (lchar+mchar+rchar)
        print(final)
        rev.append(final)
    rev.reverse()
    rev.pop(0)
    for i in range(len(rev)):
        print(rev[i])
    
        



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
