import random

def getData():
    """returns a random fruit"""
    FRUITS = ["apple", "banana", "strawberry"]
    idx = random.randint(0, len(FRUITS)-1)
    return FRUITS[idx]
