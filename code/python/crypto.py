#!/usr/bin/env python3

import random
import string


def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return f'\t\033[1;38m{"".join(random.sample(characters, length))}\033[m'


length = 16 # Standard password length
print('\n', password_generator(length))

while True:
    while True:
        try:
            print('\n\033[1;36mOptions\033[m\n\n1 - Regenerate Password\n2 - Change length\n3 - Exit')
            option = int(input("\nWhat's your choice? "))
            break
        except ValueError:
            print('\n\033[1;31mERROR! Enter only integers.\033[m')
    if option == 1:
        print('')
        print(password_generator(length))
    elif option == 2:
        while True:
            try:
                length = int(input('\nLength: '))
                print('')
                print(password_generator(length))
                break
            except ValueError:
                print('\n\033[1;31mERROR! Enter only integers. Max: 93.\033[m')
    elif option == 3:
        break
    else:
        print('\n\033[31mERROR! Try again.\033[m')
