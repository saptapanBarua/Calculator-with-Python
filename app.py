def addition(n1, n2):
    result=n1+n2
    print(f'{n1} + {n2} = {result}')

def subtraction(n1, n2):
    result=n1-n2
    print(f'{n1} - {n2} = {result}')

def multiplication(n1, n2):
    result=n1*n2
    print(f'{n1} * {n2} = {result}')

def division(n1, n2):
    try:
        result=n1/n2
        print(f'{n1} / {n2} = {result}')
    except ZeroDivisionError:
        print('Can\'t be divided by zero.')
        
operations={
    '1': addition,
    '2': subtraction,
    '3': multiplication,
    '4': division
}

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

    if (choice.lower()=='q'):
        break
    elif choice in operations:
        try:
            num1=float(input("Enter num1 : "))
            num2=float(input("Enter num2 : "))
            operations[choice](num1, num2)
        except ValueError:
            print('\n>>>Invalid Input. Please enter numbers only.<<<')
    else:
        print('\n>>>Invalid choice option. Please choose a valid operation.<<<')
