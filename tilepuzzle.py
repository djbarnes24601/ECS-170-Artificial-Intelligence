# import python libraries
import numpy as np
import copy


def tilepuzzle(start, goal, depth=10):
    return reverse(statesearch([start],goal,[],depth))

def statesearch(unexplored,goal,path,depth):
    depth -= 1 # the limit for our DFS tree. branches can't be longer than size of depth
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    elif depth < 0:
        return []
    else:
        if path != []:
            if head(path) in unexplored:
                for elem in unexplored:
                    if head(path) == elem:
                        unexplored.remove(elem)
                
        result = statesearch(generateNewStates(head(unexplored)),
                             goal,
                             cons(head(unexplored), path),depth)
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored),
                               goal,
                               path,depth)

## Find empty slot in matrix and return coordinates
def find_blank(currState):
    currState = np.array(currState)
    lst = []
    print("matrix:", currState)
    lst.append(np.where(currState == 0)[0][0])
    lst.append(np.where(currState == 0)[1][0])
    return lst

# Move a tile down
def move_tile_down(currState):
    print("move down")
    newState = matrix_copy(currState)
    indexLocation = find_blank(currState)
    m = indexLocation[0]
    n = indexLocation[1]
    
    if m == 0:
        return []
    else:
        newState[m][n] = newState[m - 1][n]
        newState[m - 1][n] = 0
        
        return newState
    
# Move a tile up
def move_tile_up(currState):
    print("move up")
    newState = matrix_copy(currState)
    indexLocation = find_blank(currState)
    m = indexLocation[0]
    n = indexLocation[1]
    
    if m == 2:
        return []
    else:
        newState[m][n] = newState[m + 1][n]
        newState[m + 1][n] = 0
        
        return newState
    
# Move a tile left
def move_tile_left(currState):
    print("move left")
    newState = matrix_copy(currState)
    indexLocation = find_blank(currState)
    m = indexLocation[0]
    n = indexLocation[1]
    
    if n == 2:
        return []
    else:
        newState[m][n] = newState[m][n + 1]
        newState[m][n + 1] = 0
        
        return newState
    
# Move a tile right
def move_tile_right(currState):
    print("move right")
    newState = matrix_copy(currState)
    indexLocation = find_blank(currState)
    m = indexLocation[0]
    n = indexLocation[1]
    
    if n == 0:
        return []
    else:
        newState[m][n] = newState[m][n - 1]
        newState[m][n - 1] = 0
        
        return newState


# Generate all possible moves you can make on the board
def generateNewStates(currState):
    lst = []
    lst.append(move_tile_up(currState))
    lst.append(move_tile_down(currState))
    lst.append(move_tile_left(currState))
    lst.append(move_tile_right(currState))
    lst2 = [x for x in lst if x != []] # remove the empty lists or impossible moves
    return lst2

# Utility
def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst

def matrix_copy(matrix):
    return copy.deepcopy(matrix)


# Test Cases
# uncomment the test cases below and try them out :)

#tilepuzzle([[2,8,3],[1,0,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]])
#tilepuzzle([[2,8,3],[1,0,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]], 32)
#tilepuzzle([[0,1,3],[4,2,5],[7,8,6]],[[1,2,3],[4,5,6],[7,8,0]])