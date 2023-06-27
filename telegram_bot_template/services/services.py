import random
from lexicon.lexicon_ru import LEXICON_RU

def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])
