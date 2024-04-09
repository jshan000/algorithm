def solution(friends, gifts):
    
    answer = 0
    
    # Draw take table by dict
    dic_take = {}
    dic_count = {}
    for i in friends:
        dic_count[i] = 0
        temp = {}
        for j in friends:
            temp[j] = 0
        dic_take[i] = temp
    
    # Fill in take table
    for i in range(len(gifts)):
        dic_take[gifts[i].split()[1]][gifts[i].split()[0]] += 1
    
    # Follow condition
    # . 1) Compare count give-take count between 2 friends.
    # .. 1.1) If not same, more giver take gift --> count + 1
    # .. 1.2) Else if same(include both 0), Compare give-take count among all friends
    # ... 1.2.1) If not same, more giver take gift --> count + 1
    # ... 1.2.2) Else if same, no-action
    # . 2) check max of count and return
    
    for i in range(len(friends)):
        a = friends[i]
        for j in range(len(friends) - i - 1):
            b = friends[i+j+1]
            # Note that dic_take[a][b] is count of that a take gift by b
            if(dic_take[a][b] == dic_take[b][a]):
                temp_a = 0
                temp_b = 0
                for k in friends:
                    temp_a += dic_take[a][k]
                    temp_a -= dic_take[k][a]
                    temp_b += dic_take[b][k]
                    temp_b -= dic_take[k][b]
                if temp_a == temp_b:
                    continue
                elif temp_a < temp_b:
                    dic_count[a] += 1
                elif temp_a > temp_b:
                    dic_count[b] += 1
            elif(dic_take[a][b] < dic_take[b][a]):
                dic_count[a] += 1
            elif(dic_take[a][b] > dic_take[b][a]):
                dic_count[b] += 1
            
                    
    for i in dic_count:
        if answer < dic_count[i]:
            answer = dic_count[i]
        
    return answer

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends,gifts))
