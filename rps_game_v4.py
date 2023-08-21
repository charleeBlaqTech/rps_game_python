import sys
import random
from enum import Enum


def rps(player_name= "playerOne"):
    game_count  = 0
    player_win  = {'score': 0, 'name': "YOU WON"}
    python_win  = {'score': 0, 'name': "PYTHON WON"}
    tie_game    = {'score': 0, 'name': "GAME WAS TIED"}

    def play_game():
        nonlocal player_name
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("\nNEW GAME BEGINS FROM HERE\n")
        playerInput= input(f'{player_name} pick a choice between the three values\n1. Rock\n2. Paper\n3. Scissors\n\n');
        if playerInput not in ['1','2','3']:
            print(f'\n\n{player_name} you can only pick 1, 2 or 3')
            return play_game()
        
        computerChoice= random.choice('123');

        player= int(playerInput);
        computer= int(computerChoice);


        def decide_winner(player, computer):
            nonlocal player_win 
            nonlocal python_win 
            nonlocal tie_game
            if player == computer:
                tie_game['score'] += 1
                return(f'you picked {str(RPS(player)).replace("RPS.", "")} and Python picked {str(RPS(computer)).replace("RPS.", "")}:\n so it is a tie game 👏👏👏');
            elif player == 1 and computer == 3:
                player_win['score'] += 1
                return(f'you picked {str(RPS(player)).replace("RPS.", "")} and Python picked {str(RPS(computer)).replace("RPS.", "")}:\n YOU WIN!!! 🏆');
            elif player == 1 and computer == 2:
                player_win['score'] += 1
                return(f'you picked {str(RPS(player)).replace("RPS.", "")} and Python picked {str(RPS(computer)).replace("RPS.", "")}:\n YOU WIN!!! 🏆');
            elif player == 3 and computer == 2:
                player_win['score'] += 1
                return(f'you picked {str(RPS(player)).replace("RPS.", "")} and Python picked {str(RPS(computer)).replace("RPS.", "")}:\n YOU WIN!!! 🏆');
            else:
                python_win["score"] +=1
                return(f'you picked {str(RPS(player)).replace("RPS.", "")} and Python picked {str(RPS(computer)).replace("RPS.", "")}:\n 🐍 PYTHON WINs!!! 🏆');
        
        game_result= decide_winner(player, computer);
        print(game_result)
        nonlocal game_count
        game_count +=1

        if(game_count <= 1):
            print(f'\n{player_name} you have played this game {game_count} time\n')
        else:
            print(f'\n{player_name} you have played this game {game_count} times\n')

        def display_scores(score):
            if(score['score'] == 1):
                return(f'{score["name"]}: {score["score"]} time\n')
            elif(score['score'] < 1):
                return(f'{score["name"]}: NONE\n')
            else:
                return(f'{score["name"]}: {score["score"]} times\n')
        print(display_scores(player_win))
        print(display_scores(python_win))
        print(display_scores(tie_game))

        print(f'\n\n{player_name} do you want to play again?')
        while True:
            play_again = input(f'\n{player_name} please choose Y for yes\nchoose N for no\n');
            if play_again.lower() not in ['y','n']:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_game()      
        else:
            print(f'\n\n{player_name} Thanks for playing 🎉')
            if __name__ == "__main__":
                sys.exit('BYE!!!   👋')
            else:
                return
            
    
    return play_game






if __name__ == "__main__":
    import argparse
    parser= argparse.ArgumentParser(
        description= "Provide a personalize game experience"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required= True, help="The name of the Person playing the game"
    )

    args= parser.parse_args();

    rock_paper_scissors= rps(args.name)
    rock_paper_scissors()

