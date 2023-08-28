import random
import math
shuru =[]
maxi = 0
totalghurbe = 0
def newFun(a,b,c,d):
    if a < b and c < d:
        return True
    else:
        return False
def FCHC(shuru, totcost, pashe, maxi, totalghurbe):
    now=shuru
    notun_cost = totcost(now)
    
    xx = 0
    temp1 = []
    
    while True:
        if newFun(xx,maxi,notun_cost,totalghurbe)==False:
            break
        neighbor_posi = pashe(now)
        optimalsol = max(neighbor_posi, key=totcost)
        optimalsol_cost = totcost(optimalsol)
        if optimalsol_cost <= notun_cost:
            break
        now = optimalsol
        notun_cost = optimalsol_cost
        xx = xx + 1
        temp1.append(now)
    return now, temp1

def valid(x,y,i,j):
    if abs(x - y ) == abs(i - j) or x == y:
        return True
    else:
        return False  
def totcost(pos):
    prob = 0
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
                if valid(pos[i],pos[j],i,j):
                    prob = prob + 1
    return -prob
def pashe(pos):
    adjacencylist = []
    for i in range(len(pos)):
        for j in range(len(pos)):
            if pos[i] != j:
                notun_pos = pos[:]
                notun_pos[i] = j
                adjacencylist.append(notun_pos)
    return adjacencylist

def createlist():
    for i in range(1,12,1):
        shuru.append(i)
def SetMaxi(x):
    return x
def SetTotalGhurbe(x):
    return x
def f():
    createlist()
    maxi=SetMaxi(500)
    totalghurbe=SetTotalGhurbe(13)

    ans, temp1 = FCHC(
    shuru, totcost, pashe, maxi, totalghurbe)
    print("Optimal position : ", ans,"\nSolution:\n")
    
    for xx, pos in enumerate(temp1):
        print("Case ", xx + 1, ":", pos,
              ":", -totcost(pos))

f()
