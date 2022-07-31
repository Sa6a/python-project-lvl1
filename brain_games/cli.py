"""Greeting."""

import prompt


def welcome_user() -> None:
    """Welcome func."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
