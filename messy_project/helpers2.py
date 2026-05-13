import random

def getData():
    data = ["apple", "banana", "straewberry"]
    idx = random.randint(0, len(data)-1)
    return data[idx]
