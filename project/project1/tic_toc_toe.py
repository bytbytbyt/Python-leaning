test_board = ['#','X','O','X','O','X','O','X','O','X']

# step 1
def display_board(test_board):
    if len(test_board) == 10  and test_board[0] == '#':
        # test_board.
        cnt = 0
        print('[')
        for t in test_board[1::]:
            print(t + ' ')
            if (cnt == 3):
                cnt = 0
                print("\n")
        cnt +=1
    else:
        print("wrong board")

# step 2
def player_input():
    print("Please choose your marker ('X' or 'O')?")
    marker = ''
    marker = input().upper()
    while not (marker == 'X' or  marker == 'O'):
        print("wrong input and I give you an another choice")
        player_input()
    if marker == 'X':
        return ('X','O')
    else: 
        return ('O','X') 


def player_input2():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
player1,player2 = player_input()
print(player1 , end = "")
print(player2 , end = "")


