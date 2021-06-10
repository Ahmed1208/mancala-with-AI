def evaluate(board):
    count1 = board[7]
    count2 = board[0]
    for i in range(1, int(len(board)/2)):
        count1 += board[i]
        count2 += board[i+7]
    return count1 - count2