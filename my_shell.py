import os
def LIST():
    """When you enter the command 
    LIST it lists the contents of the current directory"""
    os.system("ls")

def ADD(num1, num2):
    """The ADD command will add the 
    following two numbers together and provide the result"""
    result = int(num1) + int(num2)
    return result

def HELP():
    """The HELP command provides a 
    list of commands available"""
    print("Available commands: ")
    print("1. LIST \n2. ADD \n3. EXIT")

def main():
    while True:
        x = input(">>> ")
        if x == 'EXIT':
            break
        try:
            y = eval(x) # evaluation expression in a string
            if x == "LIST":
                LIST()
            elif x == "ADD":
                num1 = input('Nr. 1: ')
                num2 = input('Nr. 2: ')
                print('Result =', ADD(num1, num2))
            elif x == "HELP":
                HELP()
            elif y: 
                print(y)
        except:
            try:
                exec(x) # executing statements in a string
            except Exception as e:
                print("error:", e)

if '__main__' == __name__:
    main()