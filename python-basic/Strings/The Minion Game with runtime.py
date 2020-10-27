def minion_game(string):

    vowel = ['A','E','I','O','U']
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if string[i] in vowel:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)   
                  
    if(stuart==kevin):
        print('Draw')
    elif(stuart>kevin):
        print('Stuart '+ str(stuart))
    elif(stuart<kevin):
        print('Kevin '+ str(kevin))
           
    return 0

        



if __name__ == '__main__':
