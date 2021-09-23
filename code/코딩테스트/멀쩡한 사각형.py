from math import gcd
def solution(w,h):
    rec = w+h-gcd(w,h)
    answer=w*h-rec
    return answer
