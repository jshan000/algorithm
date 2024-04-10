def solution(edges):
    # 막대 그래프는 처음/마지막 간선이 존재하지 않음
    # 추가된 점은 나가는 점이 2개 이상이며, 들어오는 점은 없음
    # 8자의 중앙점은 나가는점 2개, 들어오는 점 2개임.
    answer = [0,0,0,0]
    # 정보를 수집해준다.
    info = checkInfo(edges)
    
    # 우선은 정점을 쳐낸다.
    for i in info:
        if info[i][0] >= 2 and info[i][1] == 0:
            answer[0] = i
    index = 0
    for i in range(len(edges)):
        if edges[index][0] == answer[0]:
            del edges[index]
            continue
        index += 1
    
    #8자와 막대를 삭제합니다.
    info = checkInfo(edges)
    ls_eight = []
    for i in info:
        if info[i][0] == 2:
            answer[3] += 1
            ls_eight.append(i)
    index = 0
    if bool(ls_eight):
        target = ls_eight[0]
        count = 0
        while(bool(ls_eight)):
            for i,j in edges:
                if i == target:
                    target = j
                    if target == ls_eight[0]:
                        if count < 1:
                            count += 1
                        else:
                            del ls_eight[0]
                            if bool(ls_eight):
                                target = ls_eight[0]
                            count = 0
                    edges.remove([i,j])
    
    info = checkInfo(edges)
    
    print(info)
    
    return answer

def checkInfo(ls):
    info = {}
    if not ls:
        return 0
    for a,b in ls:
        if (a in info):
            info[a][0] += 1
        else:
            info[a] = [1,0]
        if (b in info):
            info[b][1] += 1
        else:
            info[b] = [0,1]
            
    return info

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))