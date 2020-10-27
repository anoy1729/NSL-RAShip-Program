def count_substring(string, sub_string):
    s = string
    sub = sub_string
    count=0
    for i in range(0,len(s)):
        if(s[i]==sub[0] and s[i:(i+len(sub))]==sub):
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
