def solution(numbers, target):
    Sum=[0]
    answer=0
    for i in numbers:
        tmp=[]
        for j in Sum:
            tmp.append(j+i)
            tmp.append(j-i)
        Sum=tmp
    for check in Sum:
        if(check==target):
            answer+=1
    return answer
        
