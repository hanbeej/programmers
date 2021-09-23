def solution(scoville, K):
    check=0
    while True:
        scoville.sort()
        if(scoville[0]>=K):
            break
        elif(len(scoville)<=1 and scoville[0]<=K):
            check=-1
            break
        else:
            First=scoville.pop(0)
            Second=scoville.pop(0)
            tmp=First+(2*Second)
            scoville.insert(0,tmp)
            check=check+1
    return check
