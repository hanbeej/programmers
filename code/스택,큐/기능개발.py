def solution(progresses, speeds):
    finalList=[]
    while(len(progresses)!=0):
        check=0
        progresses=[x+y for x,y in zip(progresses,speeds)]
        if progresses[0]>=100:
            for i in range(len(progresses)):
                if(progresses[0]>=100):
                    check=check+1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    break
        if(check!=0):
            finalList.append(check)
        if(speeds==[]):
            break
    return finalList
    
