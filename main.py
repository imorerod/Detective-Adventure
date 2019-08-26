
answer = input('Would you like to play? Type yes or no')

# .strip takes off possible spaces before 'yes'
if answer.lower().strip() == 'yes':

    # game starts here
    answer = input('You have reach a fork in the road. Would you like to go left or right?').lower().strip()
    if answer == 'left':
        answer = input('You encounter a grizzly bear. Would you like to run or fight?')

        if answer == 'fight':
            print('You tried to fight a grizzly? Bold; but not smart, you lose.')
        else answer == 'run':
            print('Grizzlies are pretty fast, but you were faster. Your adrenaline kicked in and you got away safely.'
                  'Good job!')


    elif answer = 'right':

    else:
        print('Invalid choice, you lose!')

else:
    print('That is too bad!')


