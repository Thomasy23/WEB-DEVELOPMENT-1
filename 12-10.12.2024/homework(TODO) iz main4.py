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
    if x >= size or y >= size:
        return False
    return True


def print_playing_field(field):
    for row in field:
        for element in row:
            print(element + " ", end="")
        print("")


def check_winner(field, size=3):
    # Check rows and columns
    for i in range(size):
        if all(field[i][j] == field[i][0] and field[i][j] != "E" for j in range(size)):
            return field[i][0]  # Row win
        if all(field[j][i] == field[0][i] and field[j][i] != "E" for j in range(size)):
            return field[0][i]  # Column win

    # Check diagonals
    if all(field[i][i] == field[0][0] and field[i][i] != "E" for i in range(size)):
        return field[0][0]  # Main diagonal win
    if all(field[i][size - 1 - i] == field[0][size - 1] and field[i][size - 1 - i] != "E" for i in range(size)):
        return field[0][size - 1]  # Anti-diagonal win

    return None  # No winner


def is_game_over(field, size=3):
    # Check if there are no empty cells
    if all(field[i][j] != "E" for i in range(size) for j in range(size)):
        return True
    # Check if there's a winner
    if check_winner(field, size) is not None:
        return True
    return False


# Main game loop
tic_tac_toe = generate_tic_tac_toe_field()
player = 'O'

while True:
    print_playing_field(tic_tac_toe)
    move = input(f"Enter your move player {player} (x,y): ")
    moves = move.split(",")
    x = int(moves[0]) - 1
    y = int(moves[1]) - 1

    if is_valid_move(x, y, size=3):
        if tic_tac_toe[x][y] == "E":
            tic_tac_toe[x][y] = player
            winner = check_winner(tic_tac_toe)
            if winner:
                print_playing_field(tic_tac_toe)
                print(f"Player {winner} wins!")
                break
            elif is_game_over(tic_tac_toe):
                print_playing_field(tic_tac_toe)
                print("It's a draw!")
                break
            # Switch player
            player = 'X' if player == 'O' else 'O'
        else:
            print("This move has already been played, try again.")
    else:
        print("Invalid move. Try again.")
