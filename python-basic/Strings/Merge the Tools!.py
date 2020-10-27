def merge_the_tools(string, k):
    s = string
    new = []
    for i in range(0,len(s),k):
        if(i+k<=len(s)):
            word = s[i:(i+k)]
            word = "".join(dict.fromkeys(word))
        new.append(word)
        

    for i in range(len(new)):
        print(new[i])

    return new

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
