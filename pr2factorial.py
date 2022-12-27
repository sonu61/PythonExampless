def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num * factorial(num-1)
  


def TrailingZeros(num):
    i=5
    count=0
    while(num//i!=0):
        count+=int(num//i)
        i=i*5
        
    return count


if  __name__ == '__main__':
    num = int(input("enter the number: "))
   # fac = factorial(num)
   # print(f"the factorial of {num} is {factorial(num)}")
    print(TrailingZeros(num))
    
    