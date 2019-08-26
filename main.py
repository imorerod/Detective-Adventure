import os
import time


def start(inv):
    print('\nYou are in front of the house. What do you want to do?')
    print('\n1: Open the door.')
    print('2: Examine the mailbox.')
    print('3: Look under the mat.')
    print('4: Look through the window.')
    print('Quit?')

    selection_list = ['1', '2', '3', '4']
    choice = select_choice(selection_list)

    if choice == '1':
        if 'key' in inv:
            os.system('clear')
            print('You open the door with the key.')
            inside(inv)
        else:
            os.system('clear')
            print('The door is locked. You will need a key.')
            time.sleep(2)
            start()

    elif choice == '2':
        os.system('clear')
        print('You open the mailbox and find a hard drive.')
        time.sleep(1)
        print('What do you want to do?')
        print('\n1: Take the hard drive and close the mailbox.')
        print('2: Close the mailbox.')

        selection_list = ['1', '2']
        choice = select_choice(selection_list)

        if choice == '1':
            inv.append('hard drive')
            print('\nYou take the hard drive and close the mailbox.')
            time.sleep(2)
            start()
        elif choice = '2'
            print('\nYou leave the hard drive and close the mailbox.')
            time.sleep(2)
            start()

    elif choice == '3':
        os.system('clear')
        print('\nThere is a key under the mat; so cliche.')
        time.sleep(1)
        print('What do you want to do?')
        print('\n1: Take the key.')
        print('2: Put the mat back.')

        selection_list = ['1', '2']
        choice = select_choice(selection_list)

        if choice == '1':
            inv.append('key')
            print('\nYou take the key and put the mat back.')
            time.sleep(2)
            start()
        elif choice = '2'
            print('\nYou leave the key and put the mat back.')
            time.sleep(2)
            start()

    elif choice == '4':
        os.system('clear')
        print('\nAs you look through the window, you see that no one is inside.')
        print('You see a computer on a desk.')
        time.sleep(2)


def select_choice(selection_list):
    choice = input('\n? ')
    if choice in selection_list:
        return choice
    elif choice.lower().strip() == 'quit':
        exit(0)
    else:
        print('Invalid answer.')
        return select_choice(selection_list)


def inside(inv):
    print('\nYou are inside the house.')


os.system('clear')
inv = ['']
start(inv)
