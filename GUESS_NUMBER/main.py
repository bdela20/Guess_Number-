import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
         guess = int(input(f'Guess a number between 1 and {x}: '))
         if guess < random_number:
             print('Sorry, guess again, Too Low.')
         elif guess > random_number:
             print('Sorry, guess again, Too High.')
        
    print('Yay, congrats. You have guess the number {random_number} correctly. ')
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guees = random.randint(low, high)
        else:   
            guees = low
        feedback = input(f'Is {guees} too high (h), too low (l), or correct (c)??')
        if feedback == 'h':
            high = guees -1 
        if feedback == 'l':
            low = guees + 1
    print(f'Yay, the computer has guessed the number {guees} correctly.')

computer_guess(10)
         
         
    