import numpy as np

class GameLogic:
    def __init__(self):
        self.history = []

    def add_result(self, multiplier):
        self.history.append(multiplier)
        if len(self.history) > 100: # n-gardiw ghir l-akhir 100 round
            self.history.pop(0)

    def calculate_probability(self, target_multiplier):
        if not self.history:
            return 0.0
        
        # Calcul m-basé 3la l-history
        wins = sum(1 for x in self.history if x >= target_multiplier)
        prob = (wins / len(self.history)) * 100
        return round(prob, 2)
