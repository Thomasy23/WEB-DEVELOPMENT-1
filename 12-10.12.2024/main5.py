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
    if x >= size or y >= size:  # Urejeno na ">= size"
        return False
    return True


def print_playing_field(field):
    for row in field:
        for element in row:
            print(element + " ", end="")
        print("")


# Funkcija, ki preveri, ali je igra končana
def is_game_done(field):
    for row in field:
        if "E" in row:
            return False
    return True

# Funkcija, ki preveri, ali je kdo zmagal


def check_winner(field):
    size = len(field)
    # Preveri vrstice
    for row in field:
        if row[0] != "E" and all(element == row[0] for element in row):
            return row[0]
    # Preveri stolpce
    for col in range(size):
        if field[0][col] != "E" and all(field[row][col] == field[0][col] for row in range(size)):
            return field[0][col]
    # Preveri glavno diagonalo
    if field[0][0] != "E" and all(field[i][i] == field[0][0] for i in range(size)):
        return field[0][0]
    # Preveri stransko diagonalo
    if field[0][size-1] != "E" and all(field[i][size-1-i] == field[0][size-1] for i in range(size)):
        return field[0][size-1]
    # Če ni zmagovalca
    return None


# Glavni program igre
tic_tac_toe = generate_tic_tac_toe_field()
player = 'O'

while True:
    print_playing_field(tic_tac_toe)
    move = input("Enter your move player {0} (x,y): ".format(player))
    moves = move.split(",")
    x = int(moves[0])-1
    y = int(moves[1])-1
    valid_move = is_valid_move(x, y, size=len(tic_tac_toe))
    if valid_move:
        if tic_tac_toe[x][y] == "E":
            tic_tac_toe[x][y] = player
            winner = check_winner(tic_tac_toe)
            if winner:
                print_playing_field(tic_tac_toe)
                print("Player {0} wins!".format(winner))
                break
            if is_game_done(tic_tac_toe):
                print_playing_field(tic_tac_toe)
                print("It's a draw!")
                break
            player = 'X' if player == 'O' else 'O'
        else:
            print("This move has already been played, try again.")
    else:
        print("Invalid move. Try again.")
