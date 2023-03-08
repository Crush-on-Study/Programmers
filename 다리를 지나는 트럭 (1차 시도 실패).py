def solution(bridge_length, weight, truck_weights): # 최대 몇대? 최대 무게? # 대기 중?
    tot = 0
    time = 0
    going = [] # 건너는 중인 트럭 박아넣기
    arrive = [] # 도착한 트럭 박아넣기   
    
    for test_case in range(20):
        if len(truck_weights)>0:
            one = truck_weights.pop(0)
            tot+=one
            if tot <= weight:
                going.append(one)
                
            elif tot>weight:
                time+=(bridge_length)*len(going)
                going = []
        else:
            break

    return time
