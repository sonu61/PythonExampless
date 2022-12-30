import random

def play():
    user   = input(" whats your 'r' for rock , 'p' for Paper ,'s' for scissors \n ")
    computer = random.choice(['r','s','p'])
    
    if user == computer:
        return 'its a tie'
    
    if is_win(user, computer):
        return 'you won'
    
    return 'you lost !'
    
    #R>S, S>P, P>R
    
def is_win(player, opponent):
     #return true if player wins
    if(player == 'r' and opponent=='s' ) or (player =='s' and opponent == 'p')or (player =='p' and opponent == 'r'):
        return True
     
     
print(play())
     
    
    
    
    

