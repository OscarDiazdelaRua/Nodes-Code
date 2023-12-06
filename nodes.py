
import copy

# Create a function that takes two graph arrays, find the best alignment

# I believe the best way to achieve this is with recursion

def interpolation(node0, node1, K, k):

    diffPerStep = abs(node1 - node0) / (K + 1)

    return (node0 + diffPerStep * k)



def startExtr(startN, secN, opGraph, position):

    
    slope = secN - startN
    
    count = 0
    sum = 0
    for i in range(0, position):

        genN = startN - slope * (position - i)
        count += 1
        sum += sim(genN, opGraph[i])

    return [sum, count, 0, 0]



def endExtr( secN, endN, opGraph, position):

    slope = endN - secN
        
    count = 0
    sum = 0
    
    for i in range(position, len(opGraph)):

        genN = endN + slope * (position + 1)      
        count += 1       
        sum += sim(genN, opGraph[i])

    return [sum, count, 0, 0]


def sim(X, Y):


    if X > Y:
        if Y == 0:
             return (Y + 1)/(X + 1)
        return Y/X


    else :
        if X == 0:
            return (X + 1)/(Y + 1)
        return X/Y


# List node key:
# [sum, count, xorigin, yorigin]


def nodeAlignment(graphx, graphy):

# Empty 2d array:

    matrix = [[[0,0,0,0] for y in range(len(graphy)+1)] for x in range(len(graphx)+1)]

    # initialize col and row

    for i in range(1, len(graphx) + 1):
            
        matrix[i][0] = startExtr(graphy[0], graphy[1], graphx, i) 

    for i in range(1, len(graphy) + 1):
            
        matrix[0][i] = startExtr(graphx[0], graphx[1], graphy, i)

    # fill in the rest of the matrix
    
    for i in range(1, len(graphx) + 1):
        for j in range(1, len(graphy) + 1):
            
            
            
           
            maxR = [0, 0, 0, 0]
 
            maxC = [0, 0, 0, 0]
            
            if (j == 1) or (i == 1):
                maxR = matrix[i - 1][j - 1]   
                        
            else:    
                
                 # Max of Row - 1
                
                for k in range(0, j):
                    
                    intrap = copy.deepcopy(matrix[i - 1][k])
                    intrap[2] = i - 1
                    intrap[3] = k
                    
                    for l in range(k, j - 1):
                        simRes = sim(interpolation(graphx[i - 2], graphx[i - 1], j - k - 1, l + 1), graphy[j - 2])
                        intrap[0] = intrap[0] + simRes
                        intrap[1] = intrap[1] + 1


                    if intrap[1] != 0:
                        if maxR[1] == 0:
                            maxR = intrap
                            
                        elif intrap[0]/intrap[1] > maxR[0]/maxR[1]:
                            maxR = intrap


                # # Max of Col - 1

        
                for k in range(0, i):
                    
                    intrap = intrap = copy.deepcopy(matrix[k][j - 1])
                    intrap[2] = k
                    intrap[3] = j - 1

                    for l in range(k, i - 1):    
                            simRes = sim(interpolation(graphy[j - 2], graphy[j - 1], i - k - 1, l + 1), graphx[i - 2])
                            intrap[0] = intrap[0] + simRes
                            intrap[1] = intrap[1] + 1

                    if intrap[1] != 0:
                            if maxC[1] == 0:
                                maxC = intrap
                                
                            elif intrap[0]/intrap[1] > maxC[0]/maxC[1]:
                                maxC = intrap



            if maxC[1] == 0 and maxR[1] == 0:
                tMax = [0, 0, 0, 0]
            elif maxC[1] == 0:
                tMax = maxR
            elif maxR[1] == 0:
                tMax = maxC
            elif maxC[0]/maxC[1] > maxR[0]/maxR[1]:
                tMax = maxC
            else:
                tMax = maxR  
            
            matrix[i][j] = [sim(graphx[i - 1], graphy[j - 1]) + tMax[0], 1 + tMax[1], tMax[2], tMax[3]]
    
   
    # Calculate result
    
    # 
    # 
    # 
    # 
    

    
     # Max of end rows
     
    maxR = [0, 0, 0, 0]
                
    for i in range(0, len(graphy) - 1):
        
        intrap = copy.deepcopy(matrix[len(graphx)][i])
        intrap[2] = len(graphx)
        intrap[3] = i
        
        for j in range(i, len(graphy) - 1):
            simRes = endExtr(graphx[-2], graphx[-1], graphy, j)
            intrap[0] = intrap[0] + simRes[0]
            intrap[1] = intrap[1] + simRes[1]


        if intrap[1] != 0:
            if maxR[1] == 0:
                maxR = intrap
                
            elif intrap[0]/intrap[1] > maxR[0]/maxR[1]:
                maxR = intrap


    # # Max of Col - 1

    maxC = [0, 0, 0, 0]

    for i in range(0, len(graphx) - 1):
        
        intrap = copy.deepcopy(matrix[i][len(graphy)])
        intrap[2] = i
        intrap[3] = len(graphy)

        for j in range(i, len(graphx) - 1):    
                simRes = endExtr(graphy[-2], graphy[-1], graphx, j)
                intrap[0] = intrap[0] + simRes[0]
                intrap[1] = intrap[1] + simRes[1]

        if intrap[1] != 0:
                if maxC[1] == 0:
                    maxC = intrap
                    
                elif intrap[0]/intrap[1] > maxC[0]/maxC[1]:
                    maxC = intrap


    testMatr = [[[0,0,0,0] for y in range(len(graphy)+1)] for x in range(len(graphx)+1)]

    for i in range(1, len(graphx) + 1):
        for j in range(1, len(graphy) + 1):
            testMatr[i][j] = matrix[i][j][0]/matrix[i][j][1]
    
    
    result = [0,0,0,0]


    if maxC[1] == 0 and maxR[1] == 0:
        tMax = [0, 0, 0, 0]
    elif maxC[1] == 0:
        tMax = maxR
    elif maxR[1] == 0:
        tMax = maxC
    elif maxC[0]/maxC[1] > maxR[0]/maxR[1]:
        tMax = maxC
    else:
        tMax = maxR  
    
    if tMax[0]/tMax[1] > matrix[len(graphx)][len(graphy)][0]/matrix[len(graphx)][len(graphy)][1]:
        result = copy.deepcopy(tMax)
    else:
        result = copy.deepcopy(matrix[len(graphx)][len(graphy)])
        result[2] = len(graphx)
        result[3] = len(graphy)
        
        
    # 
    # 
    # 
    # 
    
    # Return result as tuples:
    
    answer = []
    
    while result[2] != 0 or result[3] != 0:
        
        answer.insert(0, (result[2], result[3]))
        
        result = matrix[result[2]][result[3]]
        
    
    

    
    return answer



if __name__ == "__main__":

# Gen Test

    # graphx = [11,14,15,16,17,18]

    # graphy = [12,13,14,15,17,18]
    
    graphx = [5, 6, 8]
    graphy = [5, 6, 7, 8]

# Perfect Alignment


    # graphx = [11,13]
    
    # graphy = [11,12,13]

    # graphx = [11,12,13,14,15,16,17,18]
    
    # graphy = [11,12,13,14,15,16,17,18]
    
    # # graphx = [4, 5, 6]
    # graphy = [4, 5, 6]

    # graphx = [10, 13, 14, 15]
    # graphy = [11, 12, 13, 15]

    print(nodeAlignment(graphx, graphy))
    
    
    # CODE BEFORE CLEAR WHIPE
    
#     def recNodeAlignment(graphx, graphy):
    
#     v = recHelper(graphx, graphy, 1, 0, 0)
#     h = recHelper(graphx, graphy, 0, 1, 0)
#     d = recHelper(graphx, graphy, 1, 1, 0)
    
#     return max(v, h, d)
    
    
    
# def recHelper(grahx, graphy, x, y, raw):
    
#     if x == len(graphx) or y == len(graphy):
#         return raw
        
    
#     if x == 0:
#         raw = startExtr(graphx[0], graphx[1], graphy, y)
    
#     if y == 0:
#         raw = startExtr(graphy[0], graphy[1], graphx, x)
    
    
#     v = recHelper(graphx, graphy, x + 1, y, raw)
#     h = recHelper(graphx, graphy, x, y + 1, raw)
#     d = recHelper(graphx, graphy, x + 1, y + 1, raw)
    
#     return max(v, h, d)
    
    

# def nodeAlignment(graphx, graphy):

# # Empty 2d array:

#     matrix = [[[0,0,0,0] for x in range(len(graphx)+1)] for y in range(len(graphy)+1)]

#     # initialize col and row

#     for i in range(1, len(graphx) + 1):
            
#         matrix[i][0] = startExtr(graphy[0], graphy[1], graphx, i) 

#     for i in range(1, len(graphy) + 1):
            
#         matrix[0][i] = startExtr(graphx[0], graphx[1], graphy, i)

#     # fill in the rest of the matrix
    
#     for i in range(1, len(graphx) + 1):
#         for j in range(1, len(graphy) + 1):
            
            
            
#             # MAx of Row - 1
#             maxR = [0, 0, 0, 0]
            
#             # if (j == 1):
                
#             #     maxC = matrix[i - 1][0]   
                        
#             # else:    
                
#             for k in range(0, j):
                
#                 intrap = matrix[i - 1][k]
#                 intrap[2] = i - 1
#                 intrap[3] = k
                
#                 for l in range(k, j - 1):
#                     simRes = sim(interpolation(graphx[i - 1], graphx[i], j - k - 1, l + 1), graphy[j - 2])
#                     intrap[0] = intrap[0] + simRes
#                     intrap[1] = intrap[1] + 1


#                 if intrap[1] != 0:
#                     if maxR[1] == 0:
#                         maxR = intrap
                        
#                     elif intrap[0]/intrap[1] > maxR[0]/maxR[1]:
#                         maxR = intrap
            
            
            
            
            
#             # # Max of Col - 1
#             maxC = [0, 0, 0, 0]
            
#             # if (i == 1):
                
#             #     maxC = matrix[0][j - 1]   
                        
#             # else:    
                   
#             for k in range(0, i):
                
#                 intrap = matrix[k][j - 1]
#                 intrap[2] = k
#                 intrap[3] = j - 1

#                 for l in range(k, i - 1):    
#                         simRes = sim(interpolation(graphy[j - 1], graphy[j], i - k - 1, l + 1), graphx[i - 2])
#                         intrap[0] = intrap[0] + simRes
#                         intrap[1] = intrap[1] + 1

#             if intrap[1] != 0:
#                     if maxC[1] == 0:
#                         maxC = intrap
                        
#                     elif intrap[0]/intrap[1] > maxC[0]/maxC[1]:
#                         maxC = intrap


#             if maxC[1] == 0 and maxR[1] == 0:
#                 tMax = [0, 0, 0, 0]
#             elif maxC[1] == 0:
#                 tMax = maxR
#             elif maxR[1] == 0:
#                 tMax = maxC
#             elif maxC[0]/maxC[1] > maxR[0]/maxR[1]:
#                 tMax = maxC
#             else:
#                 tMax = maxR  
            
#             matrix[i][j] = [sim(graphx[i - 1], graphy[j - 1]) + tMax[0], 1 + tMax[1], tMax[2], tMax[3]]
    
#     # find the last row true value
    
#     for i in range(1, len(graphx)):
#         matrix[i][len(graphy)] = matrix[i][len(graphy)] + endExtr(graphy[len(graphy) - 1], graphy[len(graphy) - 2], i)
        
#     # find the last col true value
    
#     for i in range(1, len(graphy)):
#         matrix[len(graphx)][i] = matrix[len(graphx)][i] + endExtr(graphx[len(graphx) - 1], graphx[len(graphx) - 2], i)
    
#     # find the last true value
    
    
#     def BestAlign(x, y, steps):
        
#         # Check best col -1
        
#         bestC = 0
#         for i in range(0, x - 1):
#             if matrix[i][y] > bestC:
#                 bestC = matrix[i][y]
                
#         # 
#         # TODO: Backwards method. How will backtracking work?
#         # 
        
        
#         # Check best row -1
        
#         # add best to steps
        
#         # recursive call to best
    
#     return BestAlign(len(graphx) + 2, len(graphy) + 2, 0)


    