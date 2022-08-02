"""Games of Even."""

from random import randint

from brain_games.engine import engine


def get_question() -> int:
    """
    Return question use only within play_even func.

    Returns:
        int
    """
    start_num = 0
    end_num = 99
    return randint(start_num, end_num)


def get_correct_answer(number: int) -> str:
    """
    Return correct answer use only within play_even func.

    Args:
        number: question from get_question func

    Returns:
        str
    """
    return 'yes' if number % 2 == 0 else 'no'


def play_even():
    """Play even."""
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'

    engine(game_rules, get_question, get_correct_answer)
