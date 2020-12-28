# Health Project
import sys

print('Welcome to my first game!')

name = input('What is your name? ')
age = int(input('What is your age? '))

print(f'Hello {name}. You are {age} years old!')

health = 10

if age >= 18:

    print('You are old enough to play!')
    wants_to_play = input('Do you want to play? (yes/no) ')

    if wants_to_play.lower() == 'yes':
        print(f'You starting with {health} health.')
        print('Let\'s play!')

        left_or_right = input('First choice... Left or Right (left/right)')

        if left_or_right.lower() == 'left':
            ans = input(
                'Nice, you follow the path and reach a lake... Do you swim across or go around? (across/around)')

            if ans.lower() == 'around':
                print('You went around and reached the other side of the lake!')

            elif ans == 'across':
                print('You managed to go across, but were bit by a fish and lost 5 health ')
                health -= 5

            ans = input('You notice a house and a river. Which do you go? (river/house)? ')
            if ans == 'house':
                print('You go to the house and greeted by the owner.. He didn\'nt like you and lost 5 health')
                health -= 5

                if health <= 0:
                    print('You now have 0 health and you lost the game..!!')

                else:
                    print('You have survived. You won!!')

            else:
                print('You fell down in the river and lost...!!')

        else:
            print('You fell down and lost...')

    else:
        print('Cya...')
        sys.exit()

else:

    print('Yo are not old enough to play!')
