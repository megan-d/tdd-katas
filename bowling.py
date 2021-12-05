class Game(object):
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        frame_index = 0
        for frame in range(10):
            if self.rolls[frame_index] == 10:
                total_score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
            print(total_score)
        return total_score
