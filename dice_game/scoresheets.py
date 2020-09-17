class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_three_kind(self, hand):
        return self._score_set(hand, 3)

    def score_3_of_a_kind(self, hand):
        triples = []
        others = []
        for die in hand:
            if hand.count(die) == 3:
                triples.append(die)
            else:
                others.append(die)
        if len(triples) == 3 and len(others) == 2:
            score = sum(triples) + sum(others)
            return score

    def score_4_of_a_kind(self, hand):
        quads = []
        other = []
        for die in hand:
            if hand.count(die) == 4:
                quads.append(die)
            else:
                other.append(die)
        if len(quads) == 4 and len(other) == 1:
            score = sum(quads) + sum(other)
            return score

    def score_yatzy(self, hand):
        if hand[1:] == hand[:-1]:
            return 50
        else:
            return 0

    def score_fullhouse(self, hand):
        triples = []
        doubles = []
        for die in hand:
            if hand.count(die) == 3:
                triples.append(die)
            if hand.count(die) == 2:
                doubles.append(die)
        if len(triples) == 3 and len(doubles) == 2:
            return 40
        else:
            return 0

    def score_chance(self, hand):
        return sum(hand)

    def score_high_straight(self, hand):
        if len(set(hand)) == 5 and hand[4] == 6 and hand[0] == 2:
            return 40
        return 0


    def score_low_straight(self, hand):
        if len(set(hand)) == 5 and hand[4] == 5 and hand[0] == 1:
            return 30
        return 0
