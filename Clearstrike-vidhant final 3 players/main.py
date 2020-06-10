from carromBoard import CarromBoard
from player import Player
from config.settings import TURNS
import sys, argparse, os
import collections

def load_turns(filename):
    turns = list()
    try:
        with open(filename, 'r') as f_turns:
            for line in f_turns:
                if line.strip() in TURNS:
                    turns.append(line.strip())
                else:
                    raise ValueError("Invalid Turn {0} in file {1}".format(line.strip(),filename))
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        raise ValueError("{0} No such file exits".format(filename))
    
    return turns

def main(player_1_name, player_2_name,player_3_name, input_turns):

    print("Clear Strike starting!")

    print("Initializing Carrom Board")
    # Initial coin details for a Carrom Board
    coins = {
        'black_coin': 9,
        'red_coin': 1
    }

    # Initializing players
    player_1 = Player(player_1_name)
    player_2 = Player(player_2_name)
    player_3=Player(player_3_name)
    players = [player_1, player_2,player_3]

    carrom_board = CarromBoard(coins=coins, players=players)
    print("Carrom Board created")

    print("Start Playing")

    result = carrom_board.play(input_turns)
    print("Game Ended!")

    print('------ RESULTS ------')
    result = carrom_board.results()
    if result.outcome == 'Won':
        print("{0} has won the game. Final Score: {1}".format(result.player.name,result.statistics))
    elif result.outcome == 'Draw':
        print("The Game is Draw with Final score: {0}".format(result.statistics))
    print('---------------------------')

parser = argparse.ArgumentParser()
parser.add_argument("--player_1", "-p1")
parser.add_argument("--player_2", "-p2")
parser.add_argument("--player_3", "-p3")

# parser.add_argument("--output", "-o")
args = parser.parse_args()
# Check arguments
if args.player_1 ==None and args.player_2==None:
    print("You cannot call main script like this. Please provide necessary arguments via file")
    sys.exit(1)
if args.player_1 or args.player_2:
    if not (args.player_1 and args.player_2):
        print("both arguments -p1 -p2 should be present")
        sys.exit(1)
	
# load inputs turns if exists
input_turns = dict()
p1_name = 'Player 1'
p2_name = 'Player 2'
p3_name='Player 3'
if args.player_1 and args.player_2:
    head_1, tail_1 = os.path.split(args.player_1)
    head_2, tail_2 = os.path.split(args.player_2)
    head_3, tail_3 = os.path.split(args.player_3)

    p1_name = tail_1.split(".")[0]
    p2_name = tail_2.split(".")[0]
    p3_name = tail_3.split(".")[0]

    if tail_1 == tail_2:
        print("Both file name are same. As filename will be the player's name, it has to be different")
        sys.exit(1)
    input_turns[p1_name] = load_turns(args.player_1)
    input_turns[p2_name] = load_turns(args.player_2)
    input_turns[p3_name] = load_turns(args.player_3) 
 
#input_turns = collections.OrderedDict(input_turns)
input_turns=sorted(input_turns.items())
input_turns=dict(input_turns)
print(input_turns)
# Start the Game
main(p1_name, p2_name,p3_name, input_turns)
    
     
