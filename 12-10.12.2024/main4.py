# TIC TAC TOE
def generate_tic_tac_toe_field(size=3):
    tic_tac_toe = []
    for i in range(size):
        field = []
        for j in range(size):
            field.append("E")
        tic_tac_toe.append(field)

    return tic_tac_toe


def is_valid_move(x, y, size=3):
    if x < 0 or y < 0:
        return False
    if x > size or y > size:
        return False
    return True


def print_playing_field(field):
    for row in field:
        for element in row:
            print(element + " ", end="")
        print("")


tic_tac_toe = generate_tic_tac_toe_field()

player = 'O'

while True:
    print_playing_field(tic_tac_toe)
    move = input("Enter your move player {0} (x,y): ".format(player))
    moves = move.split(",")
    x = int(moves[0])-1
    y = int(moves[1])-1
    valid_move = is_valid_move(x, y)
    if valid_move:
        if tic_tac_toe[x][y] == "E":
            tic_tac_toe[x][y] = player
            if player == 'O':
                player = 'X'
            else:
                player = 'O'
        else:
            print("This move has already been played, try again.")
    else:
        print("Invalid move. Try again.")

# TODOo: Write a function that checks if we are done!
#           -> Check if any element is E
# TODOo: Write a function that checks if anybody has won! -> 0, X
#           ->
