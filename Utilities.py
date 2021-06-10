
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
