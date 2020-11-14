def fun(s):
    
    cntat = 0
    cntdot = 0
    ext = []
    username = []
    for i in range(len(s)):
        
        if(s[i]=='.'):
            cntdot += 1
            ext = s[i+1: ]
            
            
        if(s[i]=='@'):
            cntat +=1
            username = s[:i]
            for j in range(i+1,len(s)):
                
                if( s[j]=='.' or (ord(s[j])>=97 and ord(s[j])<=122) or (ord(s[j])>=48 and ord(s[j])<=57)  ):
            
                    True
             
                else:
                    return False
                
                
        if( s[i]=='@' or s[i]=='.' or s[i]=='_' or s[i]=='-' or (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=48 and ord(s[i])<=57)  ):
            
            True
             
        else:
            return False
        
    if(len(ext)>3 or cntat!=1 or cntdot!=1 or len(username)==0 ):
        return False
        
    return True
            
            
            
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
