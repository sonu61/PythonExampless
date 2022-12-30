a = int(input("enter number: \n"))
b= int(input("enter 2nd number: \n"))

try:
 
    print(a/b)
    
except ZeroDivisionError:
    print("Infinite")
    
