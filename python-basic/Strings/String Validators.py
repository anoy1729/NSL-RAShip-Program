if __name__ == '__main__':
    s = str(input())
    temp = 0
    num=alpha=digit=lower=upper = False
    for i in range(len(s)):
        if(num==False and s[i].isalnum()==True):
            num = True
            print('True')
    if(num== False):
        print('False')
    for i in range(len(s)):
        if(alpha==False and s[i].isalpha()==True):
            alpha = True
            print('True')
    if(alpha== False):
        print('False')
    for i in range(len(s)):
        if(digit==False and s[i].isdigit()==True):
            digit = True
            print('True')
    if(digit== False):
        print('False')
    for i in range(len(s)):
        if(lower==False and s[i].islower()==True):
            lower = True
            print('True')
    if(lower== False):
        print('False')
    for i in range(len(s)):
        if(upper==False and s[i].isupper()==True):
            upper = True
            print('True')
    if(upper== False):
        print('False')
            
            

    
    
