"""Game of GCD."""

from random import randint

from brain_games.engine import engine


def find_gcd(num1: int, num2: int) -> int:
    """
    Return GCD.

    Args:
        num1: int
        num2: int

    Returns:
        int
    """
    if num1 % num2 == 0:
        return num2
    return find_gcd(num2, num1 % num2)


def get_question() -> str:
    """
    Return question.

    Returns:
        str
    """
    end_num = 99
    num1 = randint(a=1, b=end_num)
    num2 = randint(a=1, b=end_num)
    return '{num1} {num2}'.format(num1=num1, num2=num2)


def get_correct_answer(expression: str) -> str:
    """
    Return correct answer.

    Args:
        expression: question from get_question func

    Returns:
        str
    """
    expression_to_list = expression.split(' ')
    num1, num2 = expression_to_list
    return str(find_gcd(int(num1), int(num2)))


def play_gcd() -> None:
    """Play to GCD."""
    game_rules = 'Find the greatest common divisor of given numbers.'

    engine(game_rules, get_question, get_correct_answer)
