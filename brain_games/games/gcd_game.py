import random
import math

from brain_games.engine import engine


def gcd_game(count=3):
    rules = 'Find the greatest common divisor of given numbers.'
    
    engine(
        lambda: f'{random.randint(0, 100)} {random.randint(0, 100)}',
        lambda question: math.gcd(*[int(num) for num in question.split(' ')]),
        rules,
        count,
    )