"""Game of Calculator."""

from random import randint

from brain_games.engine import engine


def get_question() -> str:
    """
    Return expression for question.

    Returns:
        str
    """
    end_num = 99
    num1 = randint(0, end_num)
    num2 = randint(0, end_num)
    num_for_operation = randint(0, b=2)
    if num_for_operation == 0:
        operation = '+'
    elif num_for_operation == 1:
        operation = '-'
    else:
        operation = '*'
    return '{n1} {op} {n2}'.format(n1=num1, op=operation, n2=num2)


def get_correct_answer(expression: str) -> str:
    """
    Return correct answer.

    Args:
        expression: question from get_question func

    Returns:
        str
    """
    expression_to_list = expression.split(' ')
    num1, operation, num2 = expression_to_list
    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))
    return str(int(num1) * int(num2))


def play_calc() -> None:
    """Play to calculator."""
    game_rules = 'What is the result of the expression?'

    engine(game_rules, get_question, get_correct_answer)
