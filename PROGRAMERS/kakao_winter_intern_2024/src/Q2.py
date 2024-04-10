def solution(edges):
    answer = [0,0,0,0]
    # a is start point, b is end point.
    # each point is graph except 1 point.
    # graph has 3 type, donut, bar, infinite.
    # . 0. every point have 1 or 2(infinite graph core) path
    # . 1. donut-n graph
    # .. 1.1. has n path.
    # .. 1.2. turn back to first point, what ever choose.
    # ... 1.2.1. 
    # . 2. bar-n graph
    # .. 2.1. has n-1 path.
    # .. 2.2. has just 1 point, to search other n-1 point.
    # ... 2.2.1. every point go to end-point, end-point can reach first-point by reversing path.
    # . 3. infinite-n graph
    # .. 3.0. ** only infinite graph has core point, that has 2 path
    # .. 3.1. has 2n+1 node.
    # .. 3.2. has 2n+2 path.
    # .. 3.3. turn back to first point like donut, 1 point(middle point, core) is touched twice.
    # ... 3.3.1. to distinguish donut, we can check 1 more step, when arrive first point.
    #########
    # find additional point
    # idea
    # . 0. graph exist al least 2.
    # . 1. additional point has to connect every graph.
    # .. 1.1. there is a high probability that it has more than 3 path started by 1 point.
    # .. 1.2. else if 2 path it has, it is not infinite graph core.
    point = {}
    for a,b in edges:
        point[a] = 0
        point[b] = 0
    
    for a,b in edges:
        point[a] += 1
        
    # check additional point
    count = 0
    graph = 0
    candi = []
    for a,b in point.items():
        if(b > 2):
            answer[0] = a
            graph = b
            break
        elif(b == 2):
            count += 1
            candi.append(a)
    
    infi_p = []
    donut_p = []
    bar_p = []
    # check infinite
    if(answer[0]==0 and count < 2):
        answer[0] = a
        answer[3] = 0
    elif(answer[0]==0 and count >= 2):
        # left over part of count is infinite graph
        # it can be 1 or 2 because count == 2 (count is additional point's path)
        pass
    else:
        answer[3]=count
    
    answer[3] = count
            
        
    print(point)
    return answer


def isDonut(edges, ls):
    
    pass


def isBar(edges):
    pass


edge = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edge))