import os

print("Welcome to playing our Tic-Tac-Toe game. We promise maximum fun!\n"
      "--------------------------------------------------------------\n"
      "X goes first O goes next!\n"
      "Lets roll!!!\n"
      "---------------------------")
print("-------TIC-TAC-TOE---------")


def main():
    playing = True
    turn = 0
    prev_turn = -1
    complete = False

    board = "|1||2||3|\n" \
            "|4||5||6|\n" \
            "|7||8||9|"

    layout = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", }

    def drawBoard(gameboard):
        board = f"|{layout[1]}||{layout[2]}||{layout[3]}|\n" \
                f"|{layout[4]}||{layout[5]}||{layout[6]}|\n" \
                f"|{layout[7]}||{layout[8]}||{layout[9]}|"
        print(board)

    # tracking the turn of each player
    def trackTurn(turn):
        if turn % 2 == 0:
            return "O"
        else:
            return "X"

    def checkWin(layout):
        # horizontal case
        if (layout[1] == layout[2] == layout[3]
                or layout[4] == layout[5] == layout[6]
                or layout[7] == layout[8] == layout[9]):
            return True
        # vertical cases
        elif (layout[1] == layout[4] == layout[7]
              or layout[2] == layout[5] == layout[8]
              or layout[3] == layout[6] == layout[9]):
            return True
        # diagonal cases
        elif (layout[1] == layout[5] == layout[9]
              or layout[3] == layout[5] == layout[7]):
            return True
        else:
            return False

    # game loop
    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        # draw board
        drawBoard(layout)
        # check turns
        if prev_turn == turn:
            print("Invalid position selected, please pick another.")
        prev_turn = turn
        print("Player", str((turn % 2) + 1), "'s turn: enter a number or press q to quit")
        # take user input
        spot = input("Enter a number from 1-9 to pick a spot:")
        if spot == "q":
            playing = False
            # if spot is taken
        elif str.isdigit(spot) and int(spot) in layout:
            # prevent player location override
            if not layout[int(spot)] in {"X" or "O"}:
                turn += 1
                layout[int(spot)] = trackTurn(turn)
        # checking for win
        if checkWin(layout):
            playing, complete = False, True
        # checking for draw
        if turn > 8:
            playing = False

    drawBoard(layout)
    # say the winner
    if complete:
        if trackTurn(turn) == "X":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    else:
        print("It's a tie!")

    print("Thank you for playing! Come back next time!")


if __name__ == "__main__":
    main()
