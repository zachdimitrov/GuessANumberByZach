import random

input_prompt = '> Please choose a number from [1] to [100] or [q]uit: '
user_input = input(input_prompt)
try_number = 0
guessed = False


def check_input(inp):
    input_incorrect = True
    while input_incorrect:
        if not inp.isdigit() or int(inp) < 1 or int(inp) > 100:
            input_incorrect = True
            inp = input('> please try again [1]-[100] or [q]: ')
        else:
            input_incorrect = False
    return int(inp)


while user_input != 'q':
    user_number = check_input(user_input)
    computer_number = random.randint(1, 100)
    last_number = user_number
    while True:
        if user_number == computer_number:
            print(f'Great you nailed it! The number was {user_number}!')
            print(f'You guessed it in {try_number} tries!')
            guessed = True
            break
        else:
            if user_number < computer_number:
                try_number += 1
                if last_number <= user_number:
                    last_number = 101
                user_input = input(f'No, try again with a BIGGER number [{user_number + 1}]-[{last_number - 1}]: ')
                last_number = user_number
                user_number = check_input(user_input)
            else:
                try_number += 1
                if last_number >= user_number:
                    last_number = 0
                user_input = input(f'No, try again with a SMALLER number [{last_number + 1}]-[{user_number - 1}]: ')
                last_number = user_number
                user_number = check_input(user_input)
    if guessed:
        break
