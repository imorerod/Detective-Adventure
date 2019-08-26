import time


def start(inv):
    print('\nYou are in front of the house. What do you do?')
    print('\n1: Open the door.')
    print('2: Examine the mailbox.')
    print('3: Look under the mat.')
    print('4: Look through the window.')
    print('Quit?')

    selection_list = ['1', '2', '3', '4']
    choice = select_choice(selection_list)






def select_choice(selection_list):
    choice = input('\n? ')
    if choice in selection_list
        return choice
    elif choice.lower().strip() == 'quit':
        exit(0)
    else:
        print('Invalid answer.')
        return select_choice(selection_list)





inv = ['']
start(inv)
