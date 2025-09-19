import random

from brain_games.engine import engine


def is_even(num):
    return num % 2 == 0


def even_game(count=3):
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'

    engine(
        lambda: random.randint(0, 1000),
        lambda question: 'yes' if is_even(question) else 'no',
        rules,
        count,
    )