import prompt

from brain_games.cli import welcome_user


def engine(get_question, get_answer, rules, count):
    name = welcome_user()
    print(rules)
    
    for _ in range(count):
        question = get_question()
        answer = get_answer(question)
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != str(answer):
            print(
                f'{user_answer!r} is wrong answer ;(.',
                f'Correct answer was {answer!r}.'
            )
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    
    print(f'Congratulations, {name}!')