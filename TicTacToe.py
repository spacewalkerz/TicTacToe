table = [' ']*10
def board():
    print(table[7] + '|' + table[8] + '|' + table[9])
    print('-----')
    print(table[4] + '|' + table[5] + '|' + table[6])
    print('-----')
    print(table[1] + '|' + table[2] + '|' + table[3])
# Ask for the players input
#def player_input():
player1 = input('What would you like to pick? X or O?')
while player1 != 'X' and player1 != 'O':
    player1 = input('Please pick X or O.')

# Defines players
if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'
# Player move function
def player1_move():
    board()
    player1_move = int(input('Please make your move '+ player1))
    table[player1_move] = player1
def player2_move():
    board()
    player2_move = int(input('Please make your move ' + player2))
    table[player2_move] = player2
# Win Conditions
#def win_condition():
#    if table[4] == table[5] == table[6] != ' ':
#        print('Congrats! Player ' + player1 + ' wins!')
#    elif table[4] == table[5] == table[6] != ' ':
#        print('Congrats! Player ' + table[4] + ' wins!')
#    elif table[1] == table[2] == table[3] != ' ':
#        print('Congrats! Player ' + table[1] + ' wins!')
#    elif table[7] == table[5] == table[3] != ' ':
#        print('Congrats! Player ' + table[7] + ' wins!')
#    elif table[7] == table[4] == table[1] != ' ':
#        print('Congrats! Player ' + table[7] + ' wins!')
#    elif table[1] == table[5] == table[9] != ' ':
#        print('Congrats! Player ' + table[7] + ' wins!')
#    elif table[9] == table[6] == table[3] != ' ':
#        print('Congrats! Player ' + table[7] + ' wins!')
#    elif table[8] == table[5] == table[2] != ' ':
#        print('Congrats! Player ' + table[7] + ' wins!')

def game():

    count = 0

    while count <= 9:
        player1_move()
        count = count + 1
        if count > 4:
            if table[4] == table[5] == table[6] != ' ':
                board()
                print('Congrats! Player ' + table[4] + ' wins!')
                break
            elif table[7] == table[8] == table[9] != ' ':
                board()
                print('Congrats! Player ' + table[7] + ' wins!')
                break
            elif table[1] == table[2] == table[3] != ' ':
                board()
                print('Congrats! Player ' + table[1] + ' wins!')
                break
            elif table[7] == table[5] == table[3] != ' ':
                board()
                print('Congrats! Player ' + table[7] + ' wins!')
                break
            elif table[7] == table[4] == table[1] != ' ':
                board()
                print('Congrats! Player ' + table[7] + ' wins!')
                break
            elif table[1] == table[5] == table[9] != ' ':
                board()
                print('Congrats! Player ' + table[1] + ' wins!')
                break
            elif table[9] == table[6] == table[3] != ' ':
                board()
                print('Congrats! Player ' + table[9] + ' wins!')
                break
            elif table[8] == table[5] == table[2] != ' ':
                board()
                print('Congrats! Player ' + table[8] + ' wins!')
                break
        player2_move()
        count = count + 1
        if count > 4:
            if table[4] == table[5] == table[6] != ' ':
                print('Congrats! Player ' + table[4] + ' wins!')
                break
            elif table[7] == table[8] == table[9] != ' ':
                print('Congrats! Player ' + table[7] + ' wins!')
                break
            elif table[1] == table[2] == table[3] != ' ':
                print('Congrats! Player ' + table[1] + ' wins!')
                break
            elif table[7] == table[5] == table[3] != ' ':
                print('Congrats! Player ' + table[7] + ' wins!')
                break
            elif table[7] == table[4] == table[1] != ' ':
                print('Congrats! Player ' + table[7] + ' wins!')
                break
            elif table[1] == table[5] == table[9] != ' ':
                print('Congrats! Player ' + table[1] + ' wins!')
                break
            elif table[9] == table[6] == table[3] != ' ':
                print('Congrats! Player ' + table[9] + ' wins!')
                break
            elif table[8] == table[5] == table[2] != ' ':
                print('Congrats! Player ' + table[8] + ' wins!')
                break
    else:
        board()
        print('It is a tie!')
game()

replay = input('Would you like to replay?: ')
if replay == 'Y' or replay == 'y':
    table = [' ']*10
    game()
else:
    print('Game over!')