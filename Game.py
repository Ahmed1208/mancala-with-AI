from Utilities import print_rules,print_grid,shift_the_stones\
,all_possibles,check_does_player_finish,end_board,settings
from minimax import minimax,evaluate,indexToSlot
from timeit import default_timer
from pickle import dump

player1_slots = [ 1, 2, 3, 4, 5, 6]
player2_slots = [13,12,11,10, 9, 8]

gameEnded = True

print_rules()
player_turn,steal,diff,board = settings()
print_grid(board)

while(1):
    if player_turn == "player1":
        start = default_timer()
        res = minimax(board,float("-INF"),float("INF"),0,diff,0,steal)
        boards = all_possibles(board,"player1",steal)
        ind = indexToSlot(board,boards[res[-1]][0])
        another_turn,board = shift_the_stones(ind,player_turn,board,steal)
        print_grid(board)

        if check_does_player_finish(board):
            end_board(player_turn,board)
            break

        if another_turn == False:
            player_turn = "player2"

        stop = default_timer()
        print("Time taken: {:.3f} seconds".format(stop-start))

    elif player_turn == "player2":
        val = input("your turn: ")
        if val == "save":
            with open("load.manc",'wb') as f:
                dump({'board':board,'Steal':steal,'diff':diff},f)
            print_grid(board)
            print("board saved")
            gameEnded = False
            break
        else:
            val = int(val)
        if val in player2_slots and (board[val] != 0):
            another_turn,board = shift_the_stones(val,player_turn,board,steal)
            print_grid(board)

            if check_does_player_finish(board):
                end_board(player_turn,board)
                break

            if another_turn == False :
                player_turn = "player1"

        else:
            print("try again")

if gameEnded:
    if(board[7] > board[0]):
        print("AI wins")
    elif(board[7] < board[0]):
        print("YOU WIN")
    else:
        print("Draw")
    print_grid(board)

input("Type Any Key to quit\n")