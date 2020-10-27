def minion_game(string):

    vowel = ['A','E','I','O','U']
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        new = string[i] 
        if(new[0] in vowel):
            kevin+=1
        else:
            stuart+=1

        nxt = i+1
        if nxt<len(string):
            for j in range(nxt,len(string)):
                new = new+string[j]
                if(new[0] in vowel):
                    kevin+=1
                else:
                    stuart+=1     
                  
    if(stuart==kevin):
        print('Draw')
    elif(stuart>kevin):
        print('Stuart '+ str(stuart))
    elif(stuart<kevin):
        print('Kevin '+ str(kevin))
           
    return 0

        



if __name__ == '__main__':
    s = input()
    minion_game(s)
