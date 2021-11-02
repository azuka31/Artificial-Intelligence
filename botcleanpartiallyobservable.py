def next_move(posr,posc,board):
    def distance(coordinate_a,coordinate_b):
        distance = abs(coordinate_a[1]-coordinate_b[1]) + abs(coordinate_a[0]-coordinate_b[0])
        return distance
    def whatsquadran(coordinate):
        #Quadran1
        posr = coordinate[0]
        posc = coordinate[1]

        if posr in (0,1,2) and posc in (0,1):
            return "Q1"
        #Quadran2
        elif posr in (3,4) and posc in (0,1,2):
            return "Q2"
        #Quadran3
        elif posr in (2,3,4) and posc in (3,4):
            return "Q3"
        #Quadran4
        elif posr in (0,1) and posc in (2,3,4):
            return "Q4"
        else: 
            return "CENTER"

    def coordinate_priority(arr):
        #Located in Box Edges, Hard to be seen consisting of (0,0),(0,5),(5,0),(5,5) 
        edge = [(0,0),(0,1),(0,4),(1,4),(4,0),(3,0),(4,4),(4,3)]
        shortest=min([x[0] for x in arr])
        value_in_edge = [x for x in arr if x[1] in edge]
        value_shortest = [x for x in arr if x[0] == shortest]
        
        if len(value_in_edge) != 0:
            return value_in_edge[0]
        else:
            return value_shortest[0]

    distances = list()
    bot_coordinate = (posr, posc)

    len_row = len(board)
    len_column = len(board[0])

    for i in range(len_row):
        for j in range(len_column):
            if board[i][j] == 'd':
                d_coordinate = (i,j)
                distances.append([distance(d_coordinate,bot_coordinate),d_coordinate])

    def decide(arr):
        target = [x for x in arr if whatsquadran(x[1]) == whatsquadran(bot_coordinate)]
        if len(target) == 0:
            return None
        else:
            val = coordinate_priority(target)
            if val[0] == 0:
                return "CLEAN"
            else:
                target_coordinate = val[1]
                delta_r, delta_c = target_coordinate[0]-bot_coordinate[0], target_coordinate[1]-bot_coordinate[1]

                if abs(delta_r) > abs(delta_c):
                    if delta_r < 0:
                        return "UP"
                    else:
                        return "DOWN"
                else:
                    if delta_c < 0:
                        return "LEFT"
                    else:
                        return "RIGHT"
                
    result = decide(distances)
    if result != None:
        return result
    else:
        Q_dic = {"Q1":"DOWN","Q2":"RIGHT","Q3":"UP","Q4":"LEFT","CENTER":"LEFT"}
        result = Q_dic[whatsquadran(bot_coordinate)]
        
        if bot_coordinate in [(1,2),(0,2)]:
            return "DOWN"
        else:
            return result

if __name__ == "__main__": 
    import os
    from time import sleep
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_ = next_move(pos[0], pos[1], board)
    print(next_move(pos[0], pos[1], board))
    