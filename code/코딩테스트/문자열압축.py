def solution(s):
    sList=list(s)
    sLen=len(s)
    NumList=[]
    MinList=[]
    Num=1
    for i in range(int(len(s))):
        if i !=0:
            NumList.append(i)
    while NumList:
        tmp=NumList.pop(0)
        tmpList=[]
        AList=[]
        checkNum=0
        for i in range(int(sLen/tmp)+1):
            tmpList.append(s[i*tmp:i*tmp+tmp])
        temp=int(len(tmpList)-1)
        while(tmpList):
            tmpNum=tmpList.pop(0)
            if not tmpList:
                if Num==1:
                    AList.append(tmpNum)
                else:
                    AList.append(str(Num))
                    AList.append(tmpNum)
                Num=1
            elif(tmpNum==tmpList[0]):
                Num+=1
            else:
                if Num==1:
                    AList.append(tmpNum)
                else:
                    AList.append(str(Num))
                    AList.append(tmpNum)
                Num=1
                checkNum+=1
        AList="".join(AList)
        if checkNum!=temp:
            MinList.append(int(len(AList)))
    if not MinList:
        return int(len(s))
    else:
        return min(MinList)
        

            
            
