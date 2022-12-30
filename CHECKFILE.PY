def readFile(filename):
    try:
       with open(filename,"r") as f:
            print(f.read)
            
            
    except FileNotFoundError:
        print("Sorry your file not here:(")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")