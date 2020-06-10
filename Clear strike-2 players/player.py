import os
from config.settings import *

class Player():
    def __init__(self, name):
        self.name = name
        self.total_points = 0
        self.fouls_count = 0
        self.missed_count = 0
    

    def play(self, turn_val):
        # update player's points
        self.total_points += TURNS[turn_val]['points']

        # Update foul count
        self.update_fouls(turn_val)        
        
        # update misses counts
        self.update_misses(turn_val)

        return turn_val


    def update_fouls(self, turn_val):
        if turn_val in FOUL_TURNS:
            # Increment foul_count
            self.fouls_count += 1

            # If foul count reached max foul count
            if self.fouls_count == MAX_FOUL_COUNT:
                # Update total_count
                self.total_points += FOUL_PENALTY_POINTS 
                # reset the foul count
                self.fouls_count = 0
            
            return True
        else:
            self.fouls_count = 0
        
        return False
    

    def update_misses(self, turn_val):
        if turn_val in MISSED_TURNS:
            # Increment foul_count
            self.missed_count += 1

            # If foul count reached max foul count
            if self.missed_count == MAX_MISSED_COUNT:
                # Update total_count
                self.total_points += MISSED_PENALTY_POINTS 
                self.missed_count = 0
            
            return True
        else:
            # reset the missed count as current turn is not a missed turn
            self.missed_count = 0
        
        return False
    
    def __repr__(self):
        return "Player(name={0}, score={1})".format(self.name,self.total_points)
