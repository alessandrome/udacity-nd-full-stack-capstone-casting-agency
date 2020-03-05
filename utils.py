import random


def generate_uuid(length, prefix=''):
    if not prefix:
        prefix = ''
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'  # Modified base64 characters
    return prefix + ''.join(random.choices(chars, k=length))
