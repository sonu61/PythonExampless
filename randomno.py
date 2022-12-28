import random



def guess(num):
    random_Number = random.randint(1,num)
    
    guess =0
    
    while guess != random_Number:
        guess = int(input(f"guess number between 1 and {num}:\n"))
        if guess < random_Number:
            print(f'enter lager number, small number ')
            
        elif guess>random_Number:
            print("enter smaller number: ")
            
        
    print(f"yes you have guessed the number {random_Number}")
    
    
    #compute Guess Numberr :)))))

def ComputerGuess(num):
    low =1
    high = num
    feedback =' '
    while feedback!='c':
        if low != high:
            guess = random.randint(low,high)
            
            
        else:
            guess = low
            
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)")
        if feedback == 'h':
            high = guess -1
            
        elif feedback == 'l':
            low = low+1
            
    print(f'yay ! The computer guess your number, {guess}, correctly! :)')
    
    
    
ComputerGuess(10)
            