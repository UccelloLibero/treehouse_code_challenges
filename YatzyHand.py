#Now update Hand in hands.py. I'm going to use code similar to Hand.roll(2) and I want to get back an instance of Hand with two D20s rolled in it. I should then be able to call .total on the instance to get the total of the two dice.

#I'll leave the implementation of all of that up to you. I don't care how you do it, I only care that it works.

from dice import D20

class Hand(list):

    def __init__(self, size=0, die_class=D20):
        self.size = size
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @classmethod
    def roll(cls, size=2):
        return cls(size)

    @property
    def total(self):
        return sum(self)

# I've set you up with all of the code you've seen in the course. I want you to add a score_chance method to the YatzyScoresheet. It should take a hand argument. Return the sum total of the dice in the hand. For example, a Hand of [1, 2, 2, 3, 4] would return a score of 12.


class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)


    def score_chance(self, hand):
        return sum(hand)


# Great! Let's make one more scoring method! Create a score_yatzy method. If there are five dice with the same value, return 50. Otherwise, return 0.

def score_yatzy(self,hand):
    if self._score_set(hand, 5):
        return 50
    else:
        return 0        
