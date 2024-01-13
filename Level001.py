userName = str(input('entre userName : '))

userNameList = list(userName)

binaireToHexa = {
    '0' : '0000' ,
    '1' : '0001' ,
    '2' : '0010' ,
    '3' : '0011' ,
    '4' : '0100' ,
    '5' : '0101' ,
    '6' : '0110' ,
    '7' : '0111' ,
    '8' : '1000' ,
    '9' : '1001' ,
    'A' : '1010' ,
    'B' : '1011' ,
    'C' : '1100' ,
    'D' : '1101' ,
    'E' : '1110' ,
    'F' : '1111' 
}

for i in userNameList :
    codeAscki = ord(i)
    print(f'Code ascki du \'{i}\' : ' , codeAscki , end='\n')

    codeAsckiToList = list(map(int , str(codeAscki)))
    print('binaire code : ' , end=' ')
    for j in codeAsckiToList :
        print(binaireToHexa[f'{j}'] , end=' ')
    print('\n')