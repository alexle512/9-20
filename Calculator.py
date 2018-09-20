while (input("Hello, welcome to Calculator. Enter q to quit calculator app: ") != "q"):
    operation = input('''Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    while True:
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            print("Thank you!")
            break
        except ValueError:
            print("Not a valid number, try again... ")
    #addition
    if operation == "+":
        print('{0} + {1} = '.format(number_1, number_2))
        print(number_1 + number_2)
    #subtraction
    elif operation == "-":
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    #multiplication
    elif operation == "*":
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    #division
    elif operation == "/":
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print("You have not entered a valid operation")

