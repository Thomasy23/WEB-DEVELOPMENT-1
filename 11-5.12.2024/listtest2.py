tic_tac_toe = [
    ["X", "0", "X"],
    ["X", "0", "0"],
    ["X", "X", "0"],
]

third_row_first_colum = tic_tac_toe[2][0]

#tic_tac_toe[0][0] = "Bostjan"

for row in tic_tac_toe:
    for element in row:
        print(element + " ", end='')
    print()
