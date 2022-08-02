"""Games of Even."""

from random import randint

import prompt


def play_even():
    """Play even."""
    print('Welcome to the Brain Game!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_correct_answers = 0
    while count_correct_answers < 3:
        number = randint(1, 100)
        print('Question: {number}'.format(number=number))
        is_even = 'yes' if number % 2 == 0 else 'no'
        answer = prompt.string('Your answer: ')
        if answer == is_even:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(
                "'{answer}' is wrong answer ;(.".format(answer=answer),
                "Correct answer was '{is_even}'.".format(is_even=is_even),
            )
            print("Let's try again, {name}!".format(name=name))
            return

    if count_correct_answers > 2:
        print('Congratulations, {name}!'.format(name=name))
