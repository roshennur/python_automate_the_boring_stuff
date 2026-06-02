import re

password = 'Baba__1471'

def strong_password(password):

    pattern_lower = re.compile(r'[a-z]+')
    match1 = pattern_lower.search(password)

    pattern_upper = re.compile(r'[A-Z]+')
    match2 = pattern_upper.search(password)

    pattern_digit = re.compile(r'\d+')
    match3 = pattern_digit.search(password)

    pattern_longer = re.compile(r'[a-zA-Z0-9!@#$%^&*(){}|?><_]+')
    match4 = pattern_longer.findall(password)
    char_num = ''.join(match4)


    if len(char_num) < 9:
        return print('Your password must be at least 8 character\nAlso it must have at least 1: Lowercase, Uppercase, Digit')
    elif match1 == None:
        return print('Password should contain Lower case character')

    elif match2 == None:
        return print('Password must have Upper case character')

    elif match3 == None:
        return print('Your password requires at least one digit number')

    else:
        return print('It is strong password!')























