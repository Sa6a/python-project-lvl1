"""Module with Engine for mini-games."""

from typing import Callable

import prompt


def engine(
    game_rules: str,
    get_question: Callable,
    get_correct_answer: Callable,
) -> None:
    """
    Engine for mini-games.

    Args:
        game_rules: about game
        get_question: for current game
        get_correct_answer: for current game
    """
    print('Welcome to the Brain Game!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    print(game_rules)

    count_correct_answers = 0
    while count_correct_answers < 3:
        question = get_question()
        print('Question: {question}'.format(question=question))
        players_answer = prompt.string('Your answer ')
        correct_answer = get_correct_answer(question)
        if players_answer == correct_answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(
                "'{p_a}' is wrong answer ;(.".format(p_a=players_answer),
                "Correct answer was '{c_a}'.".format(c_a=correct_answer),
            )
            print("Let's try again, {name}!".format(name=name))
            return

    print('Congratulations, {name}!'.format(name=name))
