from config.settings import TURNS, COIN_TYPES, Results
from player import Player

class CarromBoard():
    def __init__(self, coins, players):
        # Check if coin type passed is valid
        if not type(coins) == dict:
            raise ValueError("Type of coins parameter should be a dict and not {0}".format(type(coins)))
        for coin in coins:
            if not coin in COIN_TYPES.keys():
                raise ValueError("{0} is not a valid coin type.".format(coin))

        # Check if type of players is a list and has only player class objects
        if not type(players) == list:
            raise ValueError("Type of players parameter should be a list and not {0}".format(type(players)))
        for player in players:
            if not type(player) == Player:
                print("One of the element in players list is not of type Player. Its of type {0}".format(type(player)))
                raise ValueError("All the element in list players should be an instance of Player class.")

        self.coins = coins
        self.players = players
        self.game_state = 'NotYetBegan'
        self.winner = None


    def play(self, input_turns=None):
        # Validate input_turns
        if not input_turns == None and not type(input_turns) == dict:
            raise ValueError("input_turns should of type dict and not {0}".format(type(input_turns)))

        # Update the game status
        self.game_state = 'InProgress'

        while(self.coin_exists()):
            for player in self.players:
                if len(input_turns[player.name])==0:
                    break
                outcome = input_turns[player.name].pop(0)
                if not self.is_turn_valid(outcome):
                    raise ValueError("Invalid Input turn in {0}.txt file".format(player.name))

                # pass input to player
                player.play(outcome)
                
                # update board's coins
                for k, v in TURNS[outcome]['coins_consumed'].items():
                    self.coins[k] -= v

                # Check if any player has won
                if self.has_winner():
                    self.game_state = 'Won'
                    return self.game_state
            if len(input_turns[player.name])==0:
                   break
        
        self.game_state = 'Draw'
        return self.game_state


    def coin_exists(self):
        for val in self.coins.values():
            if not val == 0:
                return True

        return False                


    def has_winner(self):
        points = list(self.get_current_points().values())

        print(points)

        # Get max point and remove it from points list
        winner_index = points.index(max(points))
        max_points = points.pop(winner_index)

        # Condition 1 : should have at least 5 points
        if not max_points >= 5:
            return False
        
        # Condition 2 : should have at lease 3 points more than opponent
        for point in points:
            if not max_points - 3 >= point:
                return False

        self.winner = self.players[winner_index]
        return True
    
    def get_current_points(self):
        ret = dict()
        for player in self.players:
            ret[player.name] = player.total_points
        
        return ret
    

    def is_turn_valid(self, turn_val):
        for coin, val in TURNS[turn_val]['coins_consumed'].items():
            if self.coins[coin] < val:
                print("Chosen turn {0} is not valid as {1} coin is not enough on the board.".format(turn_val,coin))
                print("{0} left on board is : {1}".format(coin,self.coins[coin]))
                return False

        return True 


    


    def results(self):
        # Adding to statistics
        statistics = "-".join(str(i) for i in self.get_current_points().values())

        if self.game_state in ['InProgress', 'Draw', 'NotYetBegan', 'Won']:
            return Results(self.game_state, self.winner, statistics)
        else:
            raise ValueError("game_state value is {0}, Which is not valid state!!".format(self.game_state))
        
