g=[0]*9
for _ in range(int(input())):
 i=0;w={"X":0,"O":0}
 for _ in range(3):
  for c in input():g[i]=c;i+=1
 try:input()
 except:0
 for i,j,k in[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
  if g[i]==g[j]==g[k]and g[i]in"XO":w[g[i]]=1
 print("yes"if(d:=g.count("X")-g.count("O"))in(0,1)and not(w["X"]and w["O"])and((not w["X"]and d==0)or(not w["O"]and d==1))else"no")