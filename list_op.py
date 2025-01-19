
def pro(n,list):
    m=n.split()
    
    if m[0]=="insert":
        m,i,n=n.split()
        list.insert(int(i),int(n))
    elif m[0]=="remove":
        list.remove(int(m[1]))
    elif m[0]=="extend":
        m,*n=n.split()
        list.extend(list(n))
    elif m[0]=="append":
   #     print(0)
        list.append(int(m[1]))
    #print(o)
        
n=int(input())
l=[45,56,5,7 ,7]
list=[]
for i in range(n):
#    print (o)
    
    m=input().strip()
    if m=="print":
        print(list)
    elif m=="sort":
        list=sorted(list )
    elif m=="pop":
        list.pop()
    elif m=="reverse":
        list=sorted(list,reverse=True )
    else :
        pro(m,list)
        
    