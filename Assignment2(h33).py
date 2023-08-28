Chess=[
['E','E','E','E','E','E','Q','E'],
['E','E','E','Q','E','E','E','E'],
['Q','E','E','E','E','E','E','E'],
['E','E','Q','E','E','E','E','E'],
['E','E','E','E','Q','E','E','E'],
['E','E','E','E','E','Q','E','E'],
['E','E','E','E','E','E','E','E'],
['E','Q','E','E','E','E','E','Q'],
]

Chess=[
['E','E','E','E','E','Q','E','E'],
['Q','E','E','E','E','E','E','E'],
['E','E','E','E','Q','E','E','E'],
['E','E','E','E','E','E','Q','E'],
['E','E','E','Q','E','E','E','E'],
['E','E','Q','E','E','E','E','E'],
['E','E','E','E','E','E','E','Q'],
['Q','E','E','E','E','E','E','E'],
]
totalRow=0
totalColumn=0

def Row(x):
    nrq=0
    rr=0
    for j in range(8):
        if Chess[x][j]=='Q':
            nrq=nrq+1
    rr=int((nrq*(nrq-1))/2)
    return rr

def Column(x):
    ncq=0
    cc=0
    for i in range(8):
        if Chess[i][x]=='Q':
            ncq=ncq+1
    cc=int((ncq*(ncq-1)/2))
    #print(" cc",cc," x",x)
    return cc

def DiagonalPair():
    crosspair=0
    ndq=0
    cross=0
    for i in range(8):
        m=i
        n=0
        ndq=0
        cross=0
        #print(m,n)
        while (m>=0 and m<8 and n>=0 and n<8):
                if Chess[m][n] == 'Q' :
                    ndq=ndq+1
                m = m+1
                n = n+1
        cross=int((ndq * (ndq - 1)) / 2);
        crosspair=crosspair+cross
        
        #print(cross)
        m=0
        n=i+1
        ndq=0
        cross=0
        #print(m,n)
        while (m>=0 and m<8 and n>=0 and n<8):
                if Chess[m][n] == 'Q' :
                    ndq=ndq+1
                m=m+1
                n=n+1
        cross=int((ndq * (ndq - 1)) / 2);
        #print(cross)
        crosspair=crosspair+cross
    return crosspair

def DiagonalPair2():
    crosspair=0
    ndq=0
    cross=0
    for i in range(8):
        m=i
        n=0
        
        ndq=0
        cross=0
        while (m>=0 and m<8 and n>=0 and n<8):
                if Chess[m][n] == 'Q' :
                    ndq=ndq+1
                m = m-1
                n = n+1
        cross=int((ndq * (ndq - 1)) / 2);
        crosspair=crosspair+cross
        
        m=7
        n=i+1
       
        ndq=0
        cross=0
        while (m>=0 and m<8 and n>=0 and n<8):
                if Chess[m][n] == 'Q' :
                    ndq=ndq+1
                m=m-1
                n=n+1
        cross=int((ndq * (ndq - 1)) / 2);
        crosspair=crosspair+cross
    return crosspair 
            

for x in range(8):
           x= Row(x)
           totalRow=totalRow+x
           y=Column(x)
           totalColumn=totalColumn+y

totDiag=DiagonalPair()+DiagonalPair2()
print(" ",totalRow," ",totalColumn," ",totDiag)
print("Total attacking pair of queens",(totalColumn+totalRow+totDiag))
