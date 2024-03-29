"""greeter.py - """

import random


def random_greeting_prefix():
    prefixes = ['Hey', 'Hi', 'Hello', 'Bonjour', 'Holla']
    return random.choice(prefixes)


def build_personalized_greeting(prefix: str, name: str) -> str:
    return f"Hello {prefix} {name}"


def build_greeting(name: str) -> str:
    return f"Hello {name}"


def greet(name: str):
    """Greet someone"""
    print(build_greeting(name))

def is_profanity(greeting: str) -> bool:
    return 'Fuck' in greeting
