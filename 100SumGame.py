"""
    Author: Mohamed Rady
    Date: 01 Mar 2022
    Email: mohamedradyahm@gmail.com
    This is '100 Sum Game', players alternate and enter a number from 1-10, the game ends when a player reaches sum 100
    and is declared the winner
"""


def get_player_input(player):
    """Gets the specified player's input

    Parameters
    ----------
    player : str
        Which player's input to receive

    Returns
    -------
    inp : int
        The player's input to add to the sum
    """
    inp = None
    while inp not in range(1, 11):
        try:
            inp = int(input("Player " + player + ": Enter a number to add to the sum (1 to 10): "))
            while inp not in range(1, 11):
                print("Input must be a digit from 1 to 10.")
                inp = int(input("Player " + player + ": Enter a number to add to the sum (1 to 10): "))
        except ValueError:
            print("Invalid number, please try again.")
    return inp


def check_win(player, game_sum):
    """Check if a player won with the current sum after the addition of last input

    Parameters
    ----------
    player : str
        The player with the last input
    game_sum : int
        The current sum after the last input addition

    Returns
    -------
    True
        if the player won
    False
        if the player did not win
    """
    print("The sum is", game_sum, "now.")
    if game_sum >= 100:
        print("Player "+player+" won!")
        return True
    print()
    return False


# Game main loop
def main():
    game_sum = 0
    while True:
        game_sum += get_player_input("One")
        if check_win("One", game_sum):
            break

        game_sum += get_player_input("Two")
        if check_win("Two", game_sum):
            break


main()
