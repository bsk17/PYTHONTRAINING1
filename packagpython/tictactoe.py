print("*******************************WELCOME TO TICTACTOE*******************************")

# first we create the default game
game = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]

# this is the condition to win
win = False
p1 = False
p2 = False


# the function to help player 1 to enter
def entryplayer1():
    print("Player 1 turn : Your value will be 1")
    r = eval(input("Enter the row from 0 to 2"))
    c = eval(input("Enter the column from 0 to 2"))
    val = eval(input("Enter 1"))

    try:
        # if a position is already filled then payer cannot fill
        if game[r][c] == "x":

            game[r][c] = val

            for i, j, k in game:
                print(i, j, k)

            # to check for wining condition
            if checkvictory(game, r, c):
                global win
                win = True
                p1 = True
                print("Player 1 wins")

        else:
            print("You cannot enter here")
            entryplayer1()

    except NameError:
        print("Please enter digit")
        entryplayer1()

    except IndexError:
        print("Please enter values from 0 to 2")
        entryplayer1()

    except:
        print("Something Went Wrong")
        entryplayer1()


# the function to help player 1 to enter
def entryplayer2():
    print("Player 2 turn : Your value will be 0")
    r = eval(input("Enter the row from 0 to 2"))
    c = eval(input("Enter the column from 0 to 2"))
    val = eval(input("Enter 0"))

    try:
        # if a position is already filled then payer cannot fill
        if game[r][c] == "x":

            game[r][c] = val

            for i, j, k in game:
                print(i, j, k)

            if checkvictory(game, r, c):
                global win
                win = True
                p2 = True
                print("Player 2 wins")
        else:
            print("You cannot enter here")
            entryplayer2()

    except NameError:
        print("Please enter digit")
        entryplayer2()

    except IndexError:
        print("Please enter values from 0 to 2")
        entryplayer2()

    except:
        print("Something Went Wrong")
        entryplayer2()


def checkvictory(game, r, c):

    # check if previous move caused a win on vertical line
    if game[0][c] == game[1][c] == game[2][c]:
        return True

    # check if previous move caused a win on horizontal line
    if game[r][0] == game[r][1] == game[r][2]:
        return True

    # check if previous move was on the main diagonal and caused a win
    if r == c and game[0][0] == game[1][1] == game[2][2]:
        return True

    # check if previous move was on the secondary diagonal and caused a win
    if r + c == 2 and game[0][2] == game[1][1] == game[2][0]:
        return True

    return False


while win != True:

    if(p2 == False):
        entryplayer1()
    if(p1 == False):
        entryplayer2()
