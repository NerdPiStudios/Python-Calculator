import sys

def check_to_quit(info):
    try:
        info.lower()
    except AttributeError:
        return
    if info.lower() == "quit":
        print('Now exiting...')
        sys.exit()
    else:
        return

def get_problem():
    while True:
        parenthesesEqual = 0
        digits = []
        operators = {}
        parentheses = {}
        digitsDelete = []

        problem = input()
        check_to_quit(problem) # Checks if user has entered quit to end the program

        for i in problem:
            if i in '0123456789()*-+/': # Adds character to digits list if it is a number, operator, or a parenthesis
                digits.append(i)

        while True:
            for i in range(0,len(digits)):
                if digits[i] == ')' and digits[i-1] == '(': # Checks if parentheses is () or )----(
                    digitsDelete.append(i) # Adds to digitsDelete list to be deleted
                    digitsDelete.append(i-1)
                if digits[i] in '123456789' and digits[i-1] == '0' and i != 0: # Checks if 0 is not needed
                    digitsDelete.append(i-1) # Adds to digitsDelete list to be deleted
            if len(digitsDelete) == 0: # Breaks loop if there is nothing left to delete
                break
            digitsDelete.sort() # Sorts and reverses list to prevent list index error when deleting
            digitsDelete.reverse()
            for i in digitsDelete: # Deletes items
                    del digits[i]
            del digitsDelete[:] # Clears digitsDelete list so the elements can be added back in the next iteration

        for i in range(0,len(digits)):
            if digits[i] in '+-*/': # If digit is operator, adds to operator dictionary
                operators[i] = digits[i]
            if digits[i] in '*-+/' and digits[i-1] in '-+/' and i != 0: # Checks if two operators are next to each other
                print('Two operators cannot be next to each other. Please enter the problem again.')
                pass
            if digits[i] == '(': # Adds to parentheses dictionary if digit is a parenthesis
                parentheses[i] = '('
                parenthesesEqual += 1
            elif digits[i] == ')':
                parentheses[i] = ')'
                parenthesesEqual -= 1

        if len(digits) == 0: # Checks if number of digits is greater than 0
            print('Please enter a problem.')
            pass
        elif len(operators) == 0: # Checks there is at least one operator
            print('Please enter a problem with an operator.')
            pass
        elif digits[0] in '+-*/' or digits[len(digits)-1] in '+-*/': # Checks that no two operators are next to eachother except exponentation (**)
            print('An operator cannot be first or last. Please enter the problem again.')
            pass
        elif parenthesesEqual != 0: # Checks that the number of parentheses is equal
            print('Please enter the problem again. The number of parentheses is not equal.')
            pass
        else:
            break

    sorted(parentheses) # Sorts parentheses and operator dictionaries and then returns them along with the digits list
    sorted(operators)
    return([digits,parentheses,operators])

def mainloop():
    print('Welcome to NPS calculator.')
    print('Type quit at any time to exit the program.')
    print('Please enter a problem.')
    while True:
        get_problem()
        print('Please enter another problem or type quit to exit.')

mainloop()
