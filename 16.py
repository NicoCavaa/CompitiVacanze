limite=int(input("Limite:"))
y=0
x=2
while(y<limite):
    for n in range(1,x+1):
        a=x*x-n*n
        b=2*x*n
        y=x*x+n*n
        if(y>limite):
            break
        if(a==0 or b==0 or y==0):
            break
        print(a,b,y)
    x=x+1