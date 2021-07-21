# Title: Random Password Generator
# Date: 07.21.2021
# Author: Caique Azzari

#!/usr/bin/env python3

import random
from time import sleep

banner = '''\033[34m
 __      __ __     __  __  __    __  __     __ __    ___ __  __  
|__) /\ (_ (_ |  |/  \|__)|  \  / _ |_ |\ ||_ |__) /\ | /  \|__) 
|   /--\__)__)|/\|\__/| \ |__/  \__)|__| \||__| \ /--\| \__/| \  
                                                                 \033[m
'''

print(banner)
length = 16


def standard(length=16):
    total = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    password = "".join(random.sample(total, length))
    print('-' * (length * 2))
    print(f'{password:^{length * 2}}')
    print('-' * (length * 2))


standard()
while True:
    option = int(input('''\n\033[36mOptions\033[m
                        1 - Regenerate Password
                        2 - Change length
                        3 - Exit
                
                        What's your choice? '''))
    sleep(1)

    if option == 1:
        print('')
        standard(length)
        sleep(1)
    elif option == 2:
        sleep(1)
        while True:
            try:
                length = int(input('\nLength: '))
                sleep(1)
                print('')
                standard(length)
                sleep(1)
                break
            except ValueError:
                print('\n\033[34mERROR! Enter only integers. Max: 93.\033[m')
            except:
                print('\n\033[34mERROR! Enter only integers. Max: 93.\033[m')
    elif option == 3:
        break
    else:
        sleep(1)
        print('\n ERROR! Try again.')
