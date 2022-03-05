#saroosh's branch to test merging
def display_board(marker):
    print("   |   |   ")
    print(f" {marker[7]} | {marker[8]} | {marker[9]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {marker[4]} | {marker[5]} | {marker[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {marker[1]} | {marker[2]} | {marker[3]} ")
    print("   |   |   ")


def player1_input():
    global player_input_list
    while True:
        try:
            player1_position = int(
                input(f"Enter the position [1-9] to place '{player1_marker}' for player 1: "))
            if player_input_list[player1_position] == " " and player1_position in range(1, 10):
                player_input_list[player1_position] = player1_marker
                check_result(player_input_list, player_dict)
                break
            elif player1_position not in range(1, 10):
                print("Please enter a valid position in range [1-9]")
            elif player_input_list[player1_position] != "":
                print("This position is already filled, Please select a different index")
        except:
            print("INVALID INPUT. PLEASE ENTER A VALID INPUT !!")


def player2_input():
    global player_input_list
    while True:
        try:
            player2_position = int(
                input(f"Enter the position [1-9] to place '{player2_marker}' for player 2: "))
            if player_input_list[player2_position] == " " and player2_position in range(1, 10):
                player_input_list[player2_position] = player2_marker
                check_result(player_input_list, player_dict)
                break
            elif player2_position not in range(1, 10):
                print("Please enter a valid position in range [1-9]")
            elif player_input_list[player2_position] != "":
                print("This position is already filled, Please select a different index")
        except:
            print("INVALID INPUT. PLEASE ENTER A VALID INPUT !!")

    return player_input_list


def check_result(player_input_list, player_dict):
    board1 = [player_input_list[1], player_input_list[2], player_input_list[3]]
    board2 = [player_input_list[3], player_input_list[6], player_input_list[9]]
    board3 = [player_input_list[7], player_input_list[8], player_input_list[9]]
    board4 = [player_input_list[1], player_input_list[4], player_input_list[7]]
    board5 = [player_input_list[1], player_input_list[5], player_input_list[9]]
    board6 = [player_input_list[3], player_input_list[5], player_input_list[7]]
    board7 = [player_input_list[2], player_input_list[5], player_input_list[8]]
    if board1.count("X") == 3 or board2.count("X") == 3 or board3.count("X") == 3 or board4.count("X") == 3 or board5.count("X") == 3 or board6.count("X") == 3 or board7.count("X") == 3:
        print(f"Congrats {player_dict['X']} ! You have won")
        return True
    elif board1.count("O") == 3 or board2.count("O") == 3 or board3.count("O") == 3 or board4.count("O") == 3 or board5.count("O") == 3 or board6.count("O") == 3 or board7.count("O") == 3:
        print(f"Congrats {player_dict['O']} ! You have won")
        return True
    elif player_input_list.count("X") == 4 and player_input_list.count("O") == 5 or player_input_list.count("X") == 5 and player_input_list.count("O") == 4:
        return "ITS A DRAW"
    else:
        return False


def marker_assign():
    while True:
        global player_dict
        player_dict = {}
        global player1_marker
        global player2_marker
        global player_input_list
        player_input_list = [" "]*10
        player1_marker = input(
            "Please select a marker 'X' or 'O' for player1: ")
        if player1_marker == "X":
            player2_marker = "O"
            print("Player1's marker is X")
            print("Player2's marker is O")
            player_dict['X'] = 'Player 1'
            player_dict['O'] = 'Player 2'
            break
        elif player1_marker == "O":
            player2_marker = "X"
            print("Player1's marker is O")
            print("Player2's marker is X")
            player_dict['O'] = 'Player 1'
            player_dict['X'] = 'Player 2'
            break
        else:
            print("Sorry I dont recognize that mark. Please select either 'X' or 'O'")


def play_game():
    while not (check_result(player_input_list, player_dict)):
        player1_input()
        display_board(player_input_list)
        if check_result(player_input_list, player_dict) == True:
            break
        elif check_result(player_input_list, player_dict) == "ITS A DRAW":
            print("IT's A DRAW")
            break
        player2_input()
        display_board(player_input_list)
        if check_result(player_input_list, player_dict) == True:
            break
        elif check_result(player_input_list, player_dict) == "ITS A DRAW":
            print("\nIT's A DRAW\n")
            break


if __name__ == "__main__":
    print("HELLO WORLD - FIRST GIT PUSH")
    print("\n-------Welcome to TicTacToe------")
    print("This is a two player game. Please note below KEYS to punch in markers for your game\n")
    demo_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_board(demo_list)
    marker_assign()
    play_game()
    player_dict.clear()
    player_input_list.clear()

    while True:
        prompt = input("Would you like to play again (Y) or (N) ? ")
        if prompt == "Y":
            marker_assign()
            play_game()
            player_dict.clear()
            player_input_list.clear()
        elif prompt == "N":
            print("GoodBye")
            break
        else:
            print("Sorry! I don't recognize that input.")
