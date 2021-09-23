from itertools import permutations
import math

def primeNum(num):
    if(num==0 or num==1):
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if(num%i==0):
            return False
    return True
        
def solution(numbers):
    NumList=[]
    numbersList=list(numbers)
    for i in range(1,len(numbersList)+1):
        SortNum=list(set(permutations(numbersList,i)))
        for j in range(len(SortNum)):
            tmp=int("".join(SortNum[j]))
            if(primeNum(tmp)==True):
                NumList.append(tmp)

    NumList=list(set(NumList)) 
    return len(NumList)


            
