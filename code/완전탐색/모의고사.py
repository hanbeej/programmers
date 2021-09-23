def solution(answers):
    Math_case1=[1,2,3,4,5]
    Math_case2=[2,1,2,3,2,4,2,5]
    Math_case3=[3,3,1,1,2,2,4,4,5,5]
    tmp=int(len(answers)/5+1)
    returnList=[]
    
    Math_case1=tmp*Math_case1
    Math_case2=tmp*Math_case2
    Math_case3=tmp*Math_case3
    Math_point1=0
    Math_point2=0
    Math_point3=0
    tmp=0

    for i in answers:
        if(Math_case1[tmp]==i):
            Math_point1=Math_point1+1
        if(Math_case2[tmp]==i):
            Math_point2=Math_point2+1
        if(Math_case3[tmp]==i):
            Math_point3=Math_point3+1
        tmp=tmp+1
    maxNum=max(Math_point1,Math_point2,Math_point3)

    if(Math_point1==maxNum):
        returnList.append(1)
    if(Math_point2==maxNum):
        returnList.append(2)
    if(Math_point3==maxNum):
        returnList.append(3)
    return returnList
        
