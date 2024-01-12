def main():
    print("Welcome to the Game App by The Games Developers")
    print("Please select a game to play:")
    print("1. ping pong")
    print("2. snake")
    print("3. x or o")

    choice = input()

    if choice == "1":
        game = "ping pong"
    elif choice == "2":
        game = "snake"
    elif choice == "3":
        game = "x or o"
    else:
        print("Invalid choice. Please try again.")
        return

    print("You have selected", game)
    print("Please select an option:")
    print("1. Start game")
    print("2. View credits")
    print("3. View instructions")
    print("4. View history")
    print("5. write highst score in game")

    option = input()

    if option == "1":
        start_game(game)
    elif option == "2":
        view_credits(game)
    elif option == "3":
        view_instructions(game)
    elif option == "4":
        view_history(game)
    elif option == "5":
        highest_score = input("What is the highest score in the game?\nWrite the name of the game beside the score\n")
        write_highest_score(highest_score)

    else:
        print("Invalid option. Please try again.")
        return

def start_game(game):
    print("Starting", game)
    if game==("ping pong"):
        import pingpong
    elif game==("snake"):
        import Snake
    elif game==("x or o"):
        import XorO
    # code to start the game here

def view_credits(game):
    print("Credits for", game)
    if game==("ping pong"):
        print("Created by: Allan Alcorn\nReleased by: Atari\nProgrammed by: Allan Alcorn\nConceptualized by: Nolan Bushnell (Atari founder)\nThe game was inspired by an earlier game called Tennis for Two, which was created by physicist William Higinbotham in 1958.")
    elif game==("snake"):
        print("Blockade was the first Snake and Ball arcade game\nIt was created by Gremlin Industries\nIt was released in 1976\nIt was designed by Ed Smith\nIt was developed by Tim Skelly")
    elif game==("x or o"):
        print("The first Tic-tac-toe arcade game was created as OXO also known as Noughts and Crosses\nIt was created by Alexander S. Douglas as part of his PhD thesis at the University of Cambridge in 1952\nIt was one of the first games created specifically for a computer and was played on EDSAC (Electronic Delay Storage Automatic Calculator) computer\nTaito released it as a coin-operated arcade game in 1973\nIt's worth noting that Tic Tac Toe, as a standalone game is simple and could have been implemented by multiple people in various ways and at different times.")
    # code to view the credits here

def view_instructions(game):
    print("Instructions for", game)
    if game==("ping pong"):
        print("player 1 use W and S for movement\nplayer 2 use up and down for movement\ntry to hit the ball with the racket\nif the ball pass the racket it will be point for the another player")
    elif game==("snake"):
        print("use UP,DOWN,RIGHT,LEFT buttons to reach the ball and get point\nif you touch the bourders or tourself the game will end")
    elif game==("x or o"):
        print("try to make a column from X letter or O letter to win the game")
    # code to view the instructions here

def view_history(game):
    print("History of", game)
    if game==("ping pong"):
        print("Created by: Allan Alcorn\nReleased by: Atari\nProgrammed by: Allan Alcorn\nConceptualized by: Nolan Bushnell (Atari founder)\nThe game was inspired by an earlier game called Tennis for Two, which was created by physicist William Higinbotham in 1958.")
    elif game==("snake"):
        print("The first popular example of snake and ball game is the Snake game that came bundled with Nokia mobile phones, developed by Finnish company Nokia in 1997\nThe concept of Snake game can be traced back to an arcade game called Blockade, which was developed by Gremlin Industries in 1976.\nThere is no clear first instance or creator of the snake and ball archetype, as it has multiple implementations.")
    elif game==("x or o"):
        print("Tic-tac-toe is an old game known by many names and played for centuries\nThe game's origins can be traced back to ancient civilizations such as Egypt, Rome and Greece\nThe first known instance of Tic-tac-toe played on a 3x3 grid was in the 19th century and was called Terni Lapilli\nIt is unclear who specifically created the electronic or computer version of the game as it is a simple concept that has been implemented multiple times.")
    # code to view the history here

def write_highest_score(score):
    with open("Highest.txt", "w") as file:
        file.write(str(score))

if __name__ == "__main__":
    main()
