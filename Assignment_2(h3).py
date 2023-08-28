Chess=[['E','E','E','E','E','Q','E','E'],
['Q','E','E','E','E','E','E','E'],
['E','E','E','E','Q','E','E','E'],
['E','E','E','E','E','E','Q','E'],
['E','E','E','Q','E','E','E','E'],
['E','E','Q','E','E','E','E','E'],
['E','E','E','E','E','E','E','Q'],
['Q','E','E','E','E','E','E','E'],]
totrow=0
totcol=0

def Row(num):
    nrq=0
    rr=0
    for j in range(8):
        if Chess[num][j]=='Q':
            nrq+=1
    rr=int((nrq*(nrq-1))/2)
    return rr

def Col(num):
    ncq=0
    cc=0
    for i in range(8):
        if Chess[i][num]=='Q':
            ncq+=1
    cc=int((ncq*(ncq-1)/2))
    #print(" Cpair",Cpair," num",num)
    return cc

def Cross():
    dd=0
    ndq=0
    tdd=0
    for i in range(8):
        x=i
        y=0
        ndq=0
        tdd=0
        #print(m,n)
        while (x>=0 and x<8 and y>=0 and y<8):
                if Chess[x][y] == 'Q' :
                    ndq+=1
                x+=1
                y+=1
        tdd=int((ndq * (ndq - 1)) / 2);
        dd=dd+tdd
        x=0
        y=i+1
        ndq=0
        tdd=0
        #print(m,n)
        while (x>=0 and x<8 and y>=0 and y<8):
                if Chess[x][y] == 'Q' :
                    ndq+=1
                x+=1
                y+=1
        tdd=int((ndq * (ndq - 1)) / 2);
        dd=dd+tdd
    return dd

def Cross2():
    dd=0
    ndq=0
    tdd=0
    for i in range(8):
        x=i
        y=0
        ndq=0
        tdd=0
        while (x>=0 and x<8 and y>=0 and y<8):
                if Chess[x][y] == 'Q' :
                    ndq+=1
                x-=1
                y+=1
        tdd=int((ndq * (ndq - 1)) / 2);
        dd=dd+tdd
        x=7
        y=i+1
        ndq=0
        tdd=0
        while (x>=0 and x<8 and y>=0 and y<8):
                if Chess[x][y] == 'Q' :
                    ndq+=1
                x-=1
                y+=1
        tdd=int((ndq * (ndq - 1)) / 2);
        dd=dd+tdd
    return dd 
            

for  p in range(8):
           totrow+=Row(p)
           totcol+=Col(p)

totdiag=Cross()+Cross2()
print("Total Pair of Queens which attacked each other are ",(totcol+totrow+totdiag))
