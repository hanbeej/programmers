import heapq
def solution(scoville, K):
    check=0
    heapq.heapify(scoville)
    while(scoville[0]<=K):
        heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
        check=check+1
        if(len(scoville)<=1 and scoville[0]<K):
            check=-1
            break
    return check
