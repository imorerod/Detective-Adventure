
answer = input('Would you like to play? Type yes or no')

# .strip takes off possible spaces before 'yes'
if answer.lower().strip() == 'yes':

    answer = input('You have reach a fork in the road. Would you like to go left or right?')

else:
    print('That is too bad!')


