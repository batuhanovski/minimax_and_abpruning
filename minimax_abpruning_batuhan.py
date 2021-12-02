import copy
from statistics import mean,mode
import sys

search_type=sys.argv[1]
f = open(sys.argv[2], "r")
n_actions=int(sys.argv[3])

#f = open("io/init_file1.txt", "r")
#n_actions=2

# DOWN - X+++ , RIGHT - Y+++


s = f.readline().split(' \n')
sizes = s[0].split(" ", 1)
size_x, size_y = int(sizes[0])-1,int(sizes[1])-1

input_board = [ [['x'] for i in range (int(sizes[0]))] for i in range(int(sizes[0]))]
util_calls=0

def boardInitialize():
    global sizes
    global input_board
    global f

    for i in range(int(sizes[0])):  #burda kare olduğunu varsaydık dikkat!
        elements=[]
        s = f.readline().split('\n')
        input_board[i]=s[0].split()

boardInitialize()

def makeMove(name,old_x,old_y,new_x,new_y,board_copy):
    board_copy[new_x][new_y]=name
    board_copy[old_x][old_y]='x'  
    return board_copy

def queen(name, board, loc_x,loc_y):
    
    global size_x
    global size_y
    possible_states=[]
    

    old_loc_x = loc_x
    old_loc_y = loc_y

    # N 

    check_up=False
    board_copy=copy.deepcopy(board)
    while loc_x!=0:
        check_up=True
        loc_x=loc_x-1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_up:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  
    
    # NE
    loc_x,loc_y=old_loc_x,old_loc_y 
    check_right_up=False
    board_copy=copy.deepcopy(board)
    while loc_x != 0 and loc_y!=size_y:
        check_right_up=True
        loc_x,loc_y=loc_x-1,loc_y+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_right_up:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

    # E 
    loc_x,loc_y=old_loc_x,old_loc_y    
    check_right=False
    board_copy=copy.deepcopy(board)
    while loc_y!=size_y:
        check_right=True
        loc_y=loc_y+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_right:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

    # SE
    loc_x,loc_y=old_loc_x,old_loc_y
    check_right_down=False
    board_copy=copy.deepcopy(board)
    while loc_x != size_x and loc_y!=size_y:
        check_right_down=True
        loc_x,loc_y=loc_x+1,loc_y+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_right_down:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))    

    # S
    loc_x,loc_y=old_loc_x,old_loc_y
    check_down=False
    board_copy=copy.deepcopy(board)
    while loc_x!=size_x:
        check_down=True
        loc_x=loc_x+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_down:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))

    # SW
    loc_x,loc_y=old_loc_x,old_loc_y    
    check_down_left=False
    board_copy=copy.deepcopy(board)
    while loc_x!=size_x and loc_y!=0:
        check_down_left=True
        loc_x,loc_y=loc_x+1,loc_y-1
        if board[loc_x][loc_y]!='x':
            break; 
    if check_down_left:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))    

    # W
    loc_x,loc_y=old_loc_x,old_loc_y
    check_left=False
    board_copy=copy.deepcopy(board)
    while loc_y!=0:
        check_left=True
        loc_y=loc_y-1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_left:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

    # NW
    loc_x,loc_y=old_loc_x,old_loc_y
    check_left_up=False
    board_copy=copy.deepcopy(board)
    while loc_x != 0 and loc_y!=0:
        check_left_up=True
        loc_x,loc_y=loc_x-1,loc_y-1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_left_up:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

   
    return possible_states

def rook(name, board, loc_x, loc_y):
    global size_x
    global size_y
    possible_states=[]
    
    old_loc_x = loc_x
    old_loc_y = loc_y


    
    # N
    check_up=False
    board_copy=copy.deepcopy(board)
    while loc_x!=0:
        check_up=True
        loc_x=loc_x-1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_up:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

            
    # E
    loc_x,loc_y=old_loc_x,old_loc_y    
    check_right=False
    board_copy=copy.deepcopy(board)
    while loc_y!=size_y:
        check_right=True
        loc_y=loc_y+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_right:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

    # S
    loc_x,loc_y=old_loc_x,old_loc_y
    check_down=False
    board_copy=copy.deepcopy(board)
    while loc_x!=size_x:
        check_down=True
        loc_x=loc_x+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_down:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))

    # W
    loc_x,loc_y=old_loc_x,old_loc_y
    check_left=False
    board_copy=copy.deepcopy(board)
    while loc_y!=0:
        check_left=True
        loc_y=loc_y-1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_left:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  






    return possible_states    

def bishop(name, board, loc_x, loc_y):

    global size_x
    global size_y
    possible_states=[]
    

    
    old_loc_x = loc_x
    old_loc_y = loc_y

    # NE
    loc_x,loc_y=old_loc_x,old_loc_y 
    check_right_up=False
    board_copy=copy.deepcopy(board)
    while loc_x != 0 and loc_y!=size_y:
        check_right_up=True
        loc_x,loc_y=loc_x-1,loc_y+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_right_up:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

    # SE
    loc_x,loc_y=old_loc_x,old_loc_y
    check_right_down=False
    board_copy=copy.deepcopy(board)
    while loc_x != size_x and loc_y!=size_y:
        check_right_down=True
        loc_x,loc_y=loc_x+1,loc_y+1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_right_down:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))          


    # SW
    loc_x,loc_y=old_loc_x,old_loc_y    
    check_down_left=False
    board_copy=copy.deepcopy(board)
    while loc_x!=size_x and loc_y!=0:
        check_down_left=True
        loc_x,loc_y=loc_x+1,loc_y-1
        if board[loc_x][loc_y]!='x':
            break; 
    if check_down_left:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))   

    # NW
    loc_x,loc_y=old_loc_x,old_loc_y
    check_left_up=False
    board_copy=copy.deepcopy(board)
    while loc_x != 0 and loc_y!=0:
        check_left_up=True
        loc_x,loc_y=loc_x-1,loc_y-1
        if board[loc_x][loc_y] != 'x':
            break;    
    if check_left_up:
        possible_states.append(makeMove(name,old_loc_x,old_loc_y,loc_x,loc_y,board_copy))  

    return possible_states        

def dist_types(name,row,col,board):
    if name[0]=='Q':
        return queen(name, board, row, col)
    elif name[0]=='R':    
        return rook(name, board, row, col)
    elif name[0]=='B':    
        return bishop(name, board, row, col)    

def utilityFinder(board):
    q1,q2,r1,r2,b1,b2= 0,0,0,0,0,0

    for row in board:
            q1+=row.count("Q1")
            q2+=row.count("Q2")
            r1+=row.count("R1")
            r2+=row.count("R2")
            b1+=row.count("B1")
            b2+=row.count("B2")
            
    return 9*(q1-q2) + 5*(r1-r2) + 3*(b1-b2)

def leaves_of_Max(board):
    global util_function_num
    utilities=[]
    states=[]
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem!= 'x':
                if elem[1] == '1':
                    states.append(dist_types(elem,i,j,board))

    states = [item for sublist in states for item in sublist]
    return states

def leaves_of_Min(board):
    states=[]
    
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem!= 'x':
                if elem[1] == '2':
                    states.append(dist_types(elem,i,j,board))       

    states = [item for sublist in states for item in sublist]
    return states

def minimax(board,is_max,iteration_num):
    global util_calls
    leaf_utilities=[]
    if is_max:
        states= leaves_of_Max(board)
    else:
        states = leaves_of_Min(board)

    if iteration_num != 2* n_actions:
        for state in states:
            if state != None:
                leaf_utilities.append(minimax(state, not is_max, iteration_num+1))
                    
    else:
        temp_utilities=[]
        for state in states:
            util_calls+=1
            temp_utilities.append(utilityFinder(state))   
        return min(temp_utilities)


    if is_max:
        if iteration_num !=1:
            return max(leaf_utilities)
        else:
            max_value=max(leaf_utilities)
            max_index=leaf_utilities.index(max_value)
            best_state=states[max_index]
            return max_value,best_state,util_calls

    else:
        return min(leaf_utilities)

def minimax_rand(board,is_max,iteration_num):
    global util_calls
    leaf_utilities=[]
    if is_max:
        states= leaves_of_Max(board)
    else:
        states = leaves_of_Min(board)

    if iteration_num != 2* n_actions:
        for state in states:
            if state != None:
                leaf_utilities.append(minimax_rand(state, not is_max, iteration_num+1))
                    
    else:
        temp_utilities=[]
        for state in states:
            util_calls+=1
            temp_utilities.append(utilityFinder(state))   
        return mean(temp_utilities)


    if is_max:
        if iteration_num !=1:
            return max(leaf_utilities)
        else:
            max_value=max(leaf_utilities)
            max_index=leaf_utilities.index(max_value)
            best_state=states[max_index]
            return max_value,best_state,util_calls

    else:
        return mean(leaf_utilities)

def ab_pruning(board,is_max,iteration_num,alpha,beta):
    global util_calls
    leaf_utilities=[]

    if iteration_num == 2*n_actions+1:  #final leaves
        util_calls+=1
        return utilityFinder(board)   

    
    if not is_max:
        best = float("inf")
        states=leaves_of_Min(board)
        for state in states:
            value = ab_pruning(state, not is_max, iteration_num+1, alpha, beta)
            best = min (value,best)
            beta = min(beta, best)
            if beta <= alpha:
                
                break

        return best            
    
    if is_max:
        best = float("-inf")
        states = leaves_of_Max(board)
        for state in states:
            value = ab_pruning(state,not is_max, iteration_num+1, alpha, beta)
            leaf_utilities.append(value)
            best = max (value,best)
            alpha = max(alpha,best)
            if beta <= alpha:
                break
        if iteration_num==1:
            index=leaf_utilities.index(best)    
            return best, states[index], util_calls

        return best    

def a_b_decision(board):

    return max_value(board,float("-inf"),float("inf"),1)

def max_value(board,alpha,beta,iteration_num):
    global util_calls


    if iteration_num==2*n_actions+1:
        util_calls+=1
        return utilityFinder(board)

    v=float("-inf")
    states = leaves_of_Max(board)


    for state in states:
        v = max(v,min_value(state,alpha,beta,iteration_num+1))
        if v >= beta:
            return v
        alpha = max(alpha,v)    
    
    return v

def min_value(board,alpha,beta,iteration_num):
    global util_calls

    v=float("inf") 
    states=leaves_of_Min(board)
    for state in states:
        v = min(v,max_value(state,alpha,beta,iteration_num+1))
        if v <= alpha:
            return v  
        beta = min(beta,v)     

    return v
    

    


def bestMove(first,second):

    temp=[]
    first_x,first_y,last_x,last_y=0,0,0,0
    for i in range(len(first)):
        for j in range(len(first)):
            if first[i][j]!=second[i][j]: 
                temp.append(first[i][j])
                temp.append(second[i][j])

    moved_elem = mode(temp)       

    for i in range(len(first)):
        for j in range(len(first)):
            if first[i][j]!=second[i][j]: 
                if first[i][j]==moved_elem:
                    first_x=i
                    first_y=j
                if second[i][j]==moved_elem:
                    last_x,last_y=i,j    

    direction=None
    if last_x==first_x and last_y>first_y:
        direction="E"
    elif last_x==first_x and last_y<first_y:
        direction="W"
    elif last_x>first_x and last_y==first_y:
        direction="S"
    elif last_x<first_x and last_y==first_y:
        direction="N"
    elif last_x<first_x and last_y<first_y:
        direction="NW"
    elif last_x<first_x and last_y>first_y:
        direction="NE"
    elif last_x>first_x and last_y<first_y:
        direction="SW"
    elif last_x>first_x and last_y>first_y:
        direction="SE"                
                        
    return moved_elem[:-1]+" " +direction

use_board= copy.deepcopy(input_board)

if search_type == "minimax":
    value, best_state, util_calls = minimax(use_board,True,1)    
elif search_type == "minimax_rand":
    value, best_state, util_calls = minimax_rand(use_board,True,1)        
elif search_type == "alpha_beta_pruning":
    value, best_state, util_calls = ab_pruning(use_board, True, 1, float("-inf"), float("+inf"))


#value, best_state, util_calls = minimax(use_board,True,1)    

print("Action: Move "+bestMove(input_board,best_state))
print("Value: " + str(format(value, '.2f')))
print("Util calls: " + str(util_calls))


