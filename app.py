def addition(n1, n2):
    result=n1+n2
    print(f'{n1}+{n2}={result}')

def subtraction(n1, n2):
    result=n1-n2
    print(f'{n1}-{n2}={result}')

def multiplication(n1, n2):
    result=n1*n2
    print(f'{n1}*{n2}={result}')

def division(n1, n2):
    if n2==0.0:
        print('Can\'t be divided by zero.')
    else:
        result=n1/n2
        print(f'{n1}/{n2}={result}')

while(True):
    print('''
**************************************
        Calculator with python
**************************************''')
    print('''
    What do you want to do?
        1. Addition (+)
        2. Substraction (-)
        3. Multiplication (*)
        4. Division (/)
        or press Q or q to exit the calculator''')
    choice=input("\nEnter your choice : ")

    if (choice=='Q' or choice=='q'):
        break
    else:
        num1=float(input("Enter num1 : "))
        num2=float(input("Enter num2 : "))
        if choice=='1':
            addition(num1, num2)
        elif choice=='2':
            subtraction(num1, num2)
        elif choice=='3':
            multiplication(num1, num2)
        elif choice=='4':
            division(num1, num2)    
        else:
            print('Invalid choice')
