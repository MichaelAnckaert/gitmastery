"""greeter.py - Simple Python module"""

def build_greeting(name: str) -> str:
    return f'Hello, {name}'

def greet(name: str):
    """Greet someone"""
    print(build_greeting(name))
