import sys
print('I am thinking of a number between 1 and 99')
secret_number = 60
guess_range = range(99)
Guess = int(input('Enter a guess: '))
if Guess == secret_number:
        print('Congrats! The number was: 60')
        sys.exit()
elif Guess < secret_number and Guess in guess_range:
        print('Guess is too low')
elif Guess > secret_number and Guess in guess_range:
        print('Guess is too high')

while True:
    Guess = int(input('Enter a new guess: '))
    if Guess == secret_number:
        print('Congrats! The number was:' + Guess)
        break
    elif Guess < secret_number and Guess in guess_range:
        print('Guess is too low')
    elif Guess > secret_number and Guess in guess_range:
        print('Guess is too high')
    elif Guess not in guess_range:
        print('Guess is out of range')


