from Utilities import all_possibles

def minimax(board, alpha, beta, depth, max_depth, next_step ,steal):
    
    if next_step == 0:
        boards = all_possibles(board,"player" + str((depth % 2)+1),steal)
    else:
        boards = [[board, False]]

    if depth == max_depth or len(boards) == 0:
        res = evaluate(board)
        if depth % 2 == 0:
            return max(res, alpha), beta,0
        else:
            return alpha, min(res, beta),0

    new_alpha = alpha
    new_beta = beta
    bs = []
    for i in boards:
        if new_alpha >= new_beta:
            return beta,alpha,0
        a,b,dummy = minimax(i[0], new_alpha, new_beta, depth+1, max_depth, i[1],steal)
        if depth % 2 == 0:
            new_alpha = max(new_alpha, b)
            bs.append(b)
        else:
            new_beta = min(new_beta, a)
            bs.append(b)
    if depth % 2 == 0:
        return new_alpha,new_beta,-max((x,-i) for i,x in enumerate(bs))[1]
    else:
        return new_alpha,new_beta,min((x,i) for i,x in enumerate(bs))[1]


def evaluate(board):
    count1 = board[7]
    count2 = board[0]
    for i in range(1, int(len(board)/2)):
        count1 += board[i]
        count2 += board[i+7]
    return count1 - count2
	
def indexToSlot(board,newboard):
    out = newboard.copy()
    for i in range(len(board)):
        out[i] = board[i] - newboard[i]
    return -max((x,-i) for i,x in enumerate(out))[1]
