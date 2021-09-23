def solution(priorities, location):
    Num=0
    locationCheck=[0 for i in range(len(priorities))]
    locationCheck[location]=1
    while True:
        if(max(priorities)<=priorities[0]):
            priorities.pop(0)
            Num=Num+1
            tmp=locationCheck.pop(0)
            if(tmp==1):
                break
        else:
            tmp=[priorities.pop(0)]
            priorities=priorities+tmp
            tmp=[locationCheck.pop(0)]
            locationCheck=locationCheck+tmp
    return Num
            
            
