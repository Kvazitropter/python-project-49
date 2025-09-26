import random

from brain_games.engine import engine


def get_progression_string(length=10):
    first = random.randint(-50, 50)
    diff = random.randint(-50, 50)
    sequence = [str(first + diff * i) for i in range(length)]
    return ' '.join(sequence).replace(random.choice(sequence), '...')


def find_missing_member(progression):
    members = progression.split(' ')
    missing_i = members.index('...')
    counts = [1 if i != missing_i else 0 for i in range(len(members))]
    m1, m2 = random.sample(members, k=2, counts=counts)
    i1, i2 = members.index(m1), members.index(m2)
    diff = (int(m2) - int(m1)) // (i2 - i1)
    return int(m2) - diff * (i2 - missing_i)


def progression_game(count=3):
    rules = 'What number is missing in the progression?'
    
    engine(
        get_progression_string,
        find_missing_member,
        rules,
        count,
    )