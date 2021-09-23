def solution(n):
    Num=[]
    while n>=1:
        if(n%3==0):
            Num.insert(0,str(4))
            n=int(n/3)-1
        else:
            tmp=n%3
            Num.insert(0,str(tmp))
            n=int(n/3)

    Num="".join(Num)
    
    return Num
            
            
            
        
