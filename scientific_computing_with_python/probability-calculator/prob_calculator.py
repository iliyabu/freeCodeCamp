import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = [x for arg in kwargs for x in [arg] * kwargs[arg]]
        self.drawn_balls = []

    def draw(self, number):
        number = len(self.contents) if number > len(self.contents) else number

        for _ in range(number):
            color = random.choice(self.contents)
            self.contents.remove(color)
            self.drawn_balls.append(color)

        return self.drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        successful = True

        for ball in expected_balls:
            if drawn_balls.count(ball) < expected_balls[ball]:
                successful = False

        if successful:
            successful_experiments += 1

    return successful_experiments / num_experiments
