import math
import random

from brain_games.engine import engine


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    stop = math.trunc(math.sqrt(num))
    for div in range(2, stop):
        if num % div == 0:
            return False
    
    return True


def prime_game(count=3):
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    
    engine(
        lambda: random.randint(-10, 100),
        lambda question: 'yes' if is_prime(question) else 'no',
        rules,
        count,
    )