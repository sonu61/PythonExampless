sum = 0
while(True):
    userInput = input("enter the item : \n")
    if (userInput!='q'):
         sum = sum + int(userInput)
         print(f"Order total so far: {sum}")
    
       
    else:
        print(f"your total bill is {sum}")
        break
        

    
    
    

    

