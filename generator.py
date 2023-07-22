import random
from string import ascii_letters, digits, punctuation

def generate_email(domaine: str = '@gmail.com', length: int = 6) -> str:
    #generating random email address for quick use
    return u'{0}{1}'.format(''.join(random.choice(ascii_letters) for i in range(length)), domaine)

print(generate_email())