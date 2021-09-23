def solution(bridge_length, weight, truck_weights):
    time =0
    truck_list=[0]*bridge_length
    while len(truck_list):
        time=time+1
        truck_list.pop(0)
        if truck_weights:
            if sum(truck_list)+truck_weights[0]<=weight:
                truck_list.append(truck_weights.pop(0))
            else:
                truck_list.append(0)
    return time
