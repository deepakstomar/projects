import random


def guess_number(x):
    random_number = random.randint(1, x)
    guess: int = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. too low.')
        elif guess > random_number:
            print('Sorry, guess again. too high.')
    print(f'Yay, you have guess {random_number} correctly!!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} number is high(H), low(L) or correct(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'computer guessed {guess} correctly.')


computer_guess(10)
