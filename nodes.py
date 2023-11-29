

# Create a function that takes two graph arrays, find the best alignment

# I believe the best way to achieve this is with recursion

def intrapolation(node0, node1, K, k):

    diffPerStep = (node1 - node0) / K

    return (node0 + diffPerStep * k)



def startExtr(startN, secN, opGraph, position):

    
    slope = secN - startN

    sum = 0
    for i in range(0, position):

        genN = startN - slope * position - i

        sum += sim(genN, opGraph[i])

    return (sum)



def endExtr(endN, secN, position):

    slope = endN - secN

    return (endN + slope * position)


def sim(X, Y):


    if X > Y:
        if Y == 0:
            return (X + 1)/(Y + 1)
        return X/Y

    else :
        if X == 0:
            return (Y + 1)/(X + 1)
        return Y/X



def nodeAlignment(graphx, graphy):

# Empty 2d array:

    matrix = [[0 for x in range(len(graphx)+1)] for y in range(len(graphy)+1)]

    # initialize col and row

    for i in range(1, len(graphx) + 1):
            
        matrix[i][0] = startExtr(graphy[i- 1], graphy[i], graphx, i) 

    for i in range(1, len(graphy) + 1):
            
        matrix[0][i] = startExtr(graphx[i- 2], graphx[i - 1], graphy, i)

    # fill in the rest of the matrix
    
    for i in range(1, len(graphx) + 1):
        for j in range(1, len(graphy) + 1):
            
            
            # Max of Col - 1
            maxC = 0
            for k in range(0, i - 1):
                
                intrap = matrix[k][j]
                for l in range(k, i - 1):
                    intrap = intrap + sim(intrapolation(graphy[j-2], graphy[j - 1], i - k - 1, l), graphx[i - 1])

                if intrap > maxC:
                    maxC = intrap
            
            # MAx of Row - 1
            maxR = 0
            for k in range(0, j - 1):
                
                intrap = matrix[i][k]
                for l in range(k, j - 1):
                    intrap = intrap + sim(intrapolation(graphx[i - 2], graphx[i - 1], j - k - 1, l), graphy[j - 1])
                    # intrap = intrap + sim(graphx[i-1], graphx[i], j - k - 1, l)
            
                if intrap > maxR:
                    maxR = intrap
            
            
            matrix[i][j] = sim(graphx[i - 1], graphy[j - 1]) + max(maxC, maxR)
    
    # find the last row true value
    
    for i in range(1, len(graphx)):
        matrix[i][len(graphy)] = matrix[i][len(graphy)] + endExtr(graphy[len(graphy) - 1], graphy[len(graphy) - 2], i)
        
    # find the last col true value
    
    for i in range(1, len(graphy)):
        matrix[len(graphx)][i] = matrix[len(graphx)][i] + endExtr(graphx[len(graphx) - 1], graphx[len(graphx) - 2], i)
    
    # find the last true value
    
    
    def BestAlign(x, y, steps):
        
        # Check best col -1
        
        bestC = 0
        for i in range(0, x - 1):
            if matrix[i][y] > bestC:
                bestC = matrix[i][y]
                
        # 
        # TODO: Backwards method. How will backtracking work?
        # 
        
        
        # Check best row -1
        
        # add best to steps
        
        # recursive call to best
    
    return BestAlign(len(graphx) + 2, len(graphy) + 2, 0)


    




if __name__ == "__main__":

    graphx = [11,14,15,16,17,18]

    graphy = [12,13,14,15,17,18]

    nodeAlignment(graphx, graphy)