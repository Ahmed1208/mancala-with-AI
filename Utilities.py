from termtables import print as Print
from pickle import load

def print_grid(board):
    board_grid = [
        ['', board[6],board[5],board[4],board[3],board[2],board[1],''],
        [board[7], '','','','','','',board[0]],
        ['', board[8],board[9],board[10],board[11],board[12],board[13],''],
    ]
    Print(board_grid)

def print_rules():

    board_grid = [
        ['', 6,5,4,3,2,1,''],
        ["Ai's mancala", '','','','','','',"Your mancala"],
        ['slots to choose from ->', 8,9,10,11,12,13,'<-'],
    ]
    
    Print(board_grid)
    return

def shift_the_stones(slot_number,player,board,steal=True):

    virtual_board = board.copy()
    player1_slots = [ 1, 2, 3, 4, 5, 6]
    player2_slots = [13,12,11,10, 9, 8]
    another_turn = False
    slots = 0
    if player == "player1":
        slots = player1_slots
    else:
        slots = player2_slots

    stones_number = virtual_board[slot_number]
    virtual_board[slot_number] = 0

    for dummy in range(stones_number):
        slot_number+=1
        if slot_number >13:
            slot_number = 0

        if ( (player == "player1" and slot_number == 0) or (player == "player2" and slot_number == 7) ):
            slot_number += 1
        virtual_board[slot_number] += 1



    if steal and ( virtual_board[slot_number] == 1 ) and ( slot_number in slots ) :
        if player == "player1":
            #first
            virtual_board[7] += virtual_board[slot_number]
            virtual_board[slot_number] = 0
            #second
            opposite_index = player1_slots.index(slot_number)
            opposite_slot_number = player2_slots[opposite_index]
            virtual_board[7] += virtual_board[opposite_slot_number]
            virtual_board[opposite_slot_number] = 0
        else:
            virtual_board[0] += virtual_board[slot_number]
            virtual_board[slot_number] = 0
            # second
            opposite_index = player2_slots.index(slot_number)
            opposite_slot_number = player1_slots[opposite_index]
            virtual_board[0] += virtual_board[opposite_slot_number]
            virtual_board[opposite_slot_number] = 0


    if ( slot_number == 7 and player == "player1" ) or ( slot_number == 0 and player == "player2" ):
        another_turn = True


    return another_turn,virtual_board

def check_does_player_finish(board):
    slots = [[ 1, 2, 3, 4, 5, 6],[13,12,11,10, 9, 8]]
    for slots_list in slots:
        sum = 0
        for x in slots_list:
            if board[x] == 0:
                sum +=1
        if sum == 6:
            return True
    return False

def end_board(player,board):
    player1_slots = [ 1, 2, 3, 4, 5, 6]
    player2_slots = [13,12,11,10, 9, 8]
    if player == "player1":
        for x in player2_slots:
            board[0] += board[x]
            board[x] = 0
    if player == "player2":
        for x in player1_slots:
            board[7] += board[x]
            board[x] = 0

def all_possibles(board,player,steal):

    possible_boards = []
    player1_slots = [ 1, 2, 3, 4, 5, 6]
    player2_slots = [13,12,11,10, 9, 8]
    slots = 0
    if player == "player1":
        slots = player1_slots
    else:
        slots = player2_slots

    for x in slots:
        virtual_board = board.copy()
        if virtual_board[x] == 0 :
            pass
        else:
            another_turn, virtual_board = shift_the_stones(x,player,virtual_board)
            if another_turn:
                possible_boards.append([virtual_board, True])
            else:
                possible_boards.append([virtual_board, False])

    return possible_boards

def settings():
    board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
    gameLoaded = False
    mode = None
    while mode == None:
        mode = input("\tn: New Game, l: Load Game\n")
        if mode == 'n':
            break
        elif mode == 'l':
            try:
                with open("load.manc",'rb') as f:
                    data = load(f)
                    board,Steal,diff = data['board'],data['Steal'],data['diff']
                    player_turn = 'player2'
                gameLoaded = True
            except:
                print("no board to be loaded, new game:")
        else:
            print("retry")

    if gameLoaded == False:
        player_turn = None
        while player_turn == None:
            whichTurn = input("\ty: AI starts, n: you start\n")
            if whichTurn == 'y':
                player_turn = "player1"
            elif whichTurn == 'n':
                player_turn = "player2"
            else:
                print("retry")
        
        Steal = None
        while Steal != True and Steal != False:
            withSteal = input("\ty: with steal, n: without steal\n")
            if withSteal == 'y':
                Steal = True
            elif withSteal == 'n':
                Steal = False
            else:
                print("retry")
        
        diff = None
        while diff == None:
            diff = input("difficulty:\n\te: easy, m: medium, h:hard\n")
            if diff == 'e':
                diff = 2
            elif diff == 'm':
                diff = 5
            elif diff == 'h':
                diff = 9
            else:
                print("retry")

    return player_turn,Steal,diff,board