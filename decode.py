generationTable={
    'parent':{
        'hasib':'rakib',
        'rakib':['sohel','rabeka'],  #hasib rakib er father , rakib,sohel and rabeka r father
        'rashid':'hasib',
        'abid':['prince','riya'],
        'prince':['ripa','sakif'],
        'riya':['sopon','suma'],

    },
    'male':['abid','prince','sakif','sopon','hasib','rakib','sohel','rashid'],
    'female':['riya','ripa','suma','rabeka']
}

def findParent(Z):
    for parent,children in generationTable['parent'].items():
        if Z in children:
            #print(parent)
            return parent



def isMale(person):
    if person in generationTable['male']:
        return True
    else:
        return False
def isFemale(person):
    if person in generationTable['female']:
        return True
    else:
        return False
def isFather(X,Y):
    if (generationTable['parent'][X]==Y or Y in generationTable['parent'][X]) and isMale(X):
        #print(f"{X} is the father of {Y}")
        return True
    else:
        #print(f"{X} is not {Y}'s father")
        return False
def isMother(X,Y):
    if (generationTable['parent'][X]==Y or Y in generationTable['parent'][X]) and isFemale(X):
        #print(f"{X} is the mother of {Y}")
        return True
    else:
        #print(f"{X} is not {Y}'s mother")
        return False
def areSiblings(X,Y):
    if (findParent(X) == findParent(Y)) and X!=Y:
        return True
    else:
        return False
def areBrother(X, Y):
    """ is X is the brother of Y"""

    if areSiblings(X, Y) and isMale(X):
        return True
    else:
        return False
def areSister(X, Y):
    if areSiblings(X, Y) and isFemale(X):
        # print(f"{X} is the sister of {Y}")
        return True
    else:
        # print(f"{X} is not {Y}'s sister")
        return False
def isUncle(X,Y):
    a=findParent(X)
    b=findParent(Y)
    c=findParent(b)

    if(a==c) and isMale(X):
        return True
    else:
        return False
def isAunty(X,Y):
    a=findParent(X)
    b=findParent(Y)
    c=findParent(b)

    if(a==c) and isFemale(X):
        return True
    else:
        return False
def isGrandParent(X,L):
    a=findParent(L)
    #print(a)
    b=findParent(a)

    if(X==b):
        return True
    else:
        return False



def findMales():
    print(generationTable['male'])
def findFemales():
    print(generationTable['female'])
def findFather(X):
    a=findParent(X)

    if isMale(a):
        print(a)
    else:
        print("not in the kb");
def findMother(X):
    a=findParent(X)

    if isFemale(a):
        print(a)
    else:
        print("not in the kb");
def findUncle(X):
    b=findParent(X)
    c=findParent(b)

    #print(generationTable['parent'][c])
    for i in generationTable['parent'][c]:
        if isMale(i):
            print(i)
def findAunty(X):
    b=findParent(X)
    c=findParent(b)

    #print(generationTable['parent'][c])
    for i in generationTable['parent'][c]:
        if isFemale(i):
            print(i)




print("1.check Relationship Status"+"\n"+"2.find the Relationship")
ans=int(input())

if ans==1:
    print("1.isMale"+"\n"+"2.isFemale"+"\n"+"3.isFather"+"\n"+"4.isMother"+"\n"+"5.areSiblings"+"\n"+"6.areBrother"+"\n"+"7.areSister"+"\n"+"8.isUncle"+"\n"+"9.isAunty"+"\n"+"10.isGrandparent")
    fnc=int(input())
    if fnc==1:
        print('enter the names')
        n1=input()
        print(isMale(n1))
    elif fnc==2:
        print('enter the names')
        n1=input()
        print(isFemale(n1))
    elif fnc==3:
        print('enter the names')
        n1,n2=input().split()
        print(isFather(n1,n2))
    elif fnc==4:
        print('enter the names')
        n1,n2=input().split()
        print(isMother(n1,n2))
    elif fnc==5:
        print('enter the names')
        n1,n2=input().split()
        print(areSiblings(n1,n2))
    elif fnc==6:
        print('enter the names')
        n1,n2=input().split()
        print(areBrother(n1,n2))
    elif fnc==7:
        print('enter the names')
        n1,n2=input().split()
        print(areSister(n1,n2))
    elif fnc==8:
        print('enter the names')
        n1,n2=input().split()
        print(isUncle(n1,n2))
    elif fnc==9:
        print('enter the names')
        n1,n2=input().split()
        print(isAunty(n1,n2))
    elif fnc==10:
        print('enter the names')
        n1,n2=input().split()
        print(isGrandParent(n1,n2))

else:
    print("1.findParent" + "\n" + "2.findMales" + "\n" + "3.findFemales"  + "\n" + "4.findFather" + "\n" + "5.findMother" + "\n" + "6.findUncle" + "\n" + "7.findAunty")
    fnc=int(input())
    if fnc==1:
        print('enter the name')
        n1=input()
        print(findParent(n1))
    elif fnc==2:
        findMales()
    elif fnc==3:
        findFemales()
    elif fnc==4:
         print('enter the name')
         n1=input()
         findFather(n1)
    elif fnc==5:
         print('enter the name')
         n1=input()
         findMother(n1)
    elif fnc==6:
         print('enter the name')
         n1=input()
         findUncle(n1)
    elif fnc==7:
         print('enter the name')
         n1=input()
         findAunty(n1)







