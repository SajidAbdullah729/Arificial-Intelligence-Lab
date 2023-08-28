def Durotto(shuru,shsh, dis):
  for j in range(12): 
   if Adj[j][0] == shuru:
    for k in range(12):
     if(Adj[k][0] == shuru and Adj[k][1] == shsh):
      dis+=Adj[k][2]
      return dis
    dis+=Adj[j][2]
    shuru=Adj[j][1]
    Durotto(shuru,shsh, dis)
  return dis


Adj=[('i','a',30),('x','y',3),('y','z',2),('z','az',30),('i','b',56),('a','c',17),('a','d',33),('b','d',25),('b','e',45),('b','f',16),('c','d',53),('c','g',38),('d','g',27),('e','g',16),('g','h',48)]

shuru=str(input("Start : "))
shsh=str(input("End : "))
dis=0
print("Difference between two nodes is : ", Durotto(shuru,shsh, dis))
