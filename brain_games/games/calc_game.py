import random

from brain_games.engine import engine


def get_expression():
    sign = random.choice('+-*')
    return f'{random.randint(0, 100)} {sign} {random.randint(0, 100)}'


def solve_expression(expression):
    num1, operator, num2 = expression.split(' ')
    match operator:
        case '+':
            return int(num1) + int(num2)
        case '-':
            return int(num1) - int(num2)
        case '*':
            return int(num1) * int(num2)


def calc_game(count=3):
    rules = 'What is the result of the expression?'

    engine(
        get_expression,
        lambda question: solve_expression(question),
        rules,
        count,
    )