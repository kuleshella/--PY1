from random import sample

PASSWORD_ALPHABET = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'


def get_random_password(length=8) -> str:
    return ''.join(sample(PASSWORD_ALPHABET, length))


print(get_random_password())
