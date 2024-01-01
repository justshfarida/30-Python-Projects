import secrets
import string

def contains_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def password_generator(length: int, symbols: bool, uppercase: bool) -> str:
    combination = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase
    combination_length = len(combination)

    # Initialize the password without the uppercase and symbol requirements
    new_password = ''
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    if uppercase and not contains_uppercase(new_password):
        index = secrets.randbelow(length)
        new_password = new_password[:index] + string.ascii_uppercase[secrets.randbelow(len(string.ascii_uppercase))] + new_password[(index+1):]

    if symbols and not contains_symbols(new_password):
        index = secrets.randbelow(length)
        new_password = new_password[:index] + string.punctuation[secrets.randbelow(len(string.punctuation))] + new_password[(index+1):]

    return new_password

if __name__ == '__main__':
    for i in range(1, 6):
        new_pass = password_generator(length=4, symbols=True, uppercase=False)
        specs = f'U {contains_uppercase(new_pass)}, S {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} {specs}')

    for i in range(6, 11):
        new_pass = password_generator(length=4, symbols=False, uppercase=True)
        specs = f'U {contains_uppercase(new_pass)}, S {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} {specs}')
