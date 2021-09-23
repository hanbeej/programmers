def solution(array, commands):
    reArray=[]
    for i in commands:
        tmp=array[i[0]-1:i[1]]
        tmp.sort()
        a=i[2]
        reArray.append(tmp[a-1])
    return reArray
