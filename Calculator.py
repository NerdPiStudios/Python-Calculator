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
        error = False

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
            if digits[i] == '(': # Adds to parentheses dictionary if digit is a parenthesis
                parentheses[i] = '('
                parenthesesEqual += 1
            elif digits[i] == ')':
                parentheses[i] = ')'
                parenthesesEqual -= 1
            if digits[i] in '+-*/': # If digit is operator, adds to operator dictionary
                operators[i] = digits[i]
            if digits[i] in '*-+/' and digits[i-1] in '-+/' and i != 0 and error == False: # Checks that no two operators are next to each other except exponentation (**)
                print('Two operators cannot be next to each other.')
                error = True
        for i in parentheses:
            if parentheses[i] == '(':
                if digits[i+1] in '+/*': # Checks all operators except - which means a negative number
                    print('An operator cannot be first or last within parentheses.')
                    error = True
                    break
            elif parentheses[i] == ')':
                if digits[i-1] in '+-/*':
                    print('An operator cannot be first or last within parentheses.')
                    error = True
                    break

        if len(digits) == 0: # Checks if number of digits is greater than 0
            print('Please enter a problem.')
            continue
        if len(operators) == 0: # Checks there is at least one operator
            print('There are no operators.')
            error = True
        if digits[0] in '+-*/' or digits[len(digits)-1] in '+-*/': # Checks that no operator is first or last
            print('An operator cannot be first or last.')
            error = True
        if parenthesesEqual != 0: # Checks that the number of parentheses is equal
            print('The number of parentheses of each type is not equal.')
            error = True
        if error == False:
            break
        print('Please enter the problem again.')

    sorted(parentheses) # Sorts parentheses and operator dictionaries and then returns them along with the digits list
    sorted(operators)
    return([digits,parentheses,operators])

def get_two_numbers(number1list, number2list):
    number1 = 0
    number2 = 0
    negative = False

    if number1list[0] == '-':
        del number1list[0]
        negative = True

    if '.' in number1list:
        number1part1 = number1list[:number1list.index('.')]
        number1part2 = number1list[number1list.index('.')+1:]
        number1part1.reverse()
        for i in range(0,len(number1part1)):
            number1 = number1 + int(number1part1[i]) * (10**i)
        for i in range(0,len(number1part2)):
            number1 = number1 + int(number1part2[i]) * (10**(-i-1))
    else:
        number1list.reverse()
        for i in range(0,len(number1list)):
            number1 = number1 + int(number1list[i]) * (10**i)

    if negative == True:
        number1list.insert(0, '-')
        number1 *= -1
        negative = False

    if number2list[0] == '-':
        del number2list[0]
        negative = True

    if '.' in number2list:
        number2part1 = number2list[:number2list.index('.')]
        number2part2 = number2list[number2list.index('.')+1:]
        number2part1.reverse()
        for i in range(0,len(number2part1)):
            number2 = number2 + int(number2part1[i]) * (10**i)
        for i in range(0,len(number2part2)):
            number2 = number2 + int(number2part2[i]) * (10**(-i-1))
    else:
        number2list.reverse()
        for i in range(0,len(number2list)):
            number2 = number2 + int(number2list[i]) * (10**i)

    if negative == True:
        number2list.insert(0, '-')
        number2 *= -1
        negative = False
    return [number1, number2]

def solve_parentheses(info):
    digits = info[0]
    parentheses = info[1]
    operators = info[2]
    parenthesesList = []

    for i in parentheses:
        parenthesesList.append(i)

    while True:
        working = []
        parenthesesList.sort()
        for i in range(0,len(parenthesesList)):
            if digits[parenthesesList[i]] == ')' and digits[parenthesesList[i-1]] == '(' and i != 0:
                working = digits[parenthesesList[i-1]+1:parenthesesList[i]]
                currentParenthesesSection = i
                break

        while True:
            operatorsWorking = []
            number1list = []
            number2list = []
            number1 = 0
            number2 = 0
            currentOperator = ''
            solution = 0

            for i in range(0,len(working)):
                if working[i] in '*+/':
                    operatorsWorking.append(i)
                elif working[i] == '-' and i != 0:
                    operatorsWorking.append(i)

            if len(operatorsWorking) == 1:
                number1list = working[:operatorsWorking[0]]
                number2list = working[operatorsWorking[0]+1:]
                print(working)
                print(number1list)
                print(number2list)
                returnedValue = get_two_numbers(number1list, number2list)
                number1 = returnedValue[0]
                number2 = returnedValue[1]

                if working[operatorsWorking[0]] == '-':
                    solution = number1-number2
                elif working[operatorsWorking[0]] == '+':
                    solution = number1+number2
                elif working[operatorsWorking[0]] == '*':
                    solution = number1*number2
                elif working[operatorsWorking[0]] == '/':
                    solution = number1/number2
                working = []
                for i in str(solution):
                    working.append(i)

                del digits[parenthesesList[currentParenthesesSection-1]:parenthesesList[currentParenthesesSection]+1]
                if parenthesesList[currentParenthesesSection-1] == 0:
                    digitsPart1 = []
                    digitsPart2 = digits
                elif parenthesesList[currentParenthesesSection] == len(digits)-1:
                    digitsPart1 = digits
                    digitsPart2 = []
                else:
                    digitsPart1 = digits[:parenthesesList[currentParenthesesSection-1]]
                    digitsPart2 = digits[parenthesesList[currentParenthesesSection-1]:]
                for i in working:
                    digitsPart1.append(i)
                digits = digitsPart1 + digitsPart2

                parenthesesList = []
                parentheses = {}
                for i in range(0,len(digits)):
                    if digits[i] == '(': # Adds to parentheses dictionary if digit is a parenthesis
                        parentheses[i] = '('
                        parenthesesList.append(i)
                    elif digits[i] == ')':
                        parentheses[i] = ')'
                        parenthesesList.append(i)
                break

            elif len(operatorsWorking) > 1:
                for i in range(0,len(operatorsWorking)):
                    if working[operatorsWorking[i]] == '*' or working[operatorsWorking[i]] == '/':
                        currentOperator = i
                        break
                for i in range(0,len(operatorsWorking)):
                    if working[operatorsWorking[i]] == '+' or working[operatorsWorking[i]] == '-' and currentOperator == '':
                        currentOperator = i

                if currentOperator == 0:
                    number1list = working[:operatorsWorking[0]]
                    number2list = working[operatorsWorking[0]+1:operatorsWorking[1]]
                elif currentOperator == len(operatorsWorking) - 1:
                    number1list = working[operatorsWorking[currentOperator-1]+1:operatorsWorking[currentOperator]]
                    number2list = working[operatorsWorking[currentOperator]+1:]
                else:
                    number1list = working[operatorsWorking[currentOperator-1]+1:operatorsWorking[currentOperator]]
                    number2list = working[operatorsWorking[currentOperator]+1:operatorsWorking[currentOperator+1]]

                print(working)
                print(number1list)
                print(number2list)
                returnedValue = get_two_numbers(number1list, number2list)
                number1 = returnedValue[0]
                number2 = returnedValue[1]

                if working[operatorsWorking[currentOperator]] == '-':
                    solution = number1-number2
                elif working[operatorsWorking[currentOperator]] == '+':
                    solution = number1+number2
                elif working[operatorsWorking[currentOperator]] == '*':
                    solution = number1*number2
                elif working[operatorsWorking[currentOperator]] == '/':
                    solution = number1/number2

                if currentOperator == 0:
                    del working[:operatorsWorking[1]]
                    workingPart1 = []
                    workingPart2 = working
                elif currentOperator == len(operatorsWorking)-1:
                    del working[operatorsWorking[currentOperator-1]+1:]
                    workingPart1 = working
                    workingPart2 = []
                else:
                    del working[operatorsWorking[currentOperator-1]+1:operatorsWorking[currentOperator+1]]
                    workingPart1 = working[:operatorsWorking[currentOperator-1]+1]
                    workingPart2 = working[operatorsWorking[currentOperator-1]+1:]
                for i in str(solution):
                    workingPart1.append(i)
                working = workingPart1 + workingPart2

            else:
                print(digits)
                return digits

def solve_program(info):
    digits = info
    while True:
        operatorsWorking = []
        number1list = []
        number2list = []
        number1 = 0
        number2 = 0
        currentOperator = ''
        solution = 0

        for i in range(0,len(digits)):
            if digits[i] in '*+/':
                operatorsWorking.append(i)
            elif digits[i] == '-' and i != 0:
                operatorsWorking.append(i)

        if len(operatorsWorking) == 1:
            number1list = digits[:operatorsWorking[0]]
            number2list = digits[operatorsWorking[0]+1:]
            returnedValue = get_two_numbers(number1list, number2list)
            number1 = returnedValue[0]
            number2 = returnedValue[1]

            if digits[operatorsWorking[0]] == '-':
                solution = number1-number2
            elif digits[operatorsWorking[0]] == '+':
                solution = number1+number2
            elif digits[operatorsWorking[0]] == '*':
                solution = number1*number2
            elif digits[operatorsWorking[0]] == '/':
                solution = number1/number2
            digits = []
            for i in str(solution):
                digits.append(i)

        elif len(operatorsWorking) > 1:
            for i in range(0,len(operatorsWorking)):
                if digits[operatorsWorking[i]] == '*' or digits[operatorsWorking[i]] == '/':
                    currentOperator = i
                    break
            for i in range(0,len(operatorsWorking)):
                if digits[operatorsWorking[i]] == '+' or digits[operatorsWorking[i]] == '-' and currentOperator == '':
                    currentOperator = i

            if currentOperator == 0:
                number1list = digits[:operatorsWorking[0]]
                number2list = digits[operatorsWorking[0]+1:operatorsWorking[1]]
            elif currentOperator == len(operatorsWorking) - 1:
                number1list = digits[operatorsWorking[currentOperator-1]+1:operatorsWorking[currentOperator]]
                number2list = digits[operatorsWorking[currentOperator]+1:]
            else:
                number1list = digits[operatorsWorking[currentOperator-1]+1:operatorsWorking[currentOperator]]
                number2list = digits[operatorsWorking[currentOperator]+1:operatorsWorking[currentOperator+1]]

            returnedValue = get_two_numbers(number1list, number2list)
            number1 = returnedValue[0]
            number2 = returnedValue[1]

            if digits[operatorsWorking[currentOperator]] == '-':
                solution = number1-number2
            elif digits[operatorsWorking[currentOperator]] == '+':
                solution = number1+number2
            elif digits[operatorsWorking[currentOperator]] == '*':
                solution = number1*number2
            elif digits[operatorsWorking[currentOperator]] == '/':
                solution = number1/number2

            if currentOperator == 0:
                del digits[:operatorsWorking[1]]
                workingPart1 = []
                workingPart2 = digits
            elif currentOperator == len(operatorsWorking)-1:
                del digits[operatorsWorking[currentOperator-1]+1:]
                workingPart1 = digits
                workingPart2 = []
            else:
                del working[operatorsWorking[currentOperator-1]+1:operatorsWorking[currentOperator+1]]
                workingPart1 = digits[:operatorsWorking[currentOperator-1]+1]
                workingPart2 = digits[operatorsWorking[currentOperator-1]+1:]

            for i in str(solution):
                workingPart1.append(i)
            digits = workingPart1 + workingPart2

        else:
            print(digits)
            digits = get_two_numbers(digits, ['1'])[0]
            print(digits)
            return digits

def mainloop():
    print('Welcome to NPS calculator.')
    print('Type quit at any time to exit the program.')
    print('Please enter a problem.')
    while True:
        print('The answer is: ' + str(solve_program(solve_parentheses(get_problem()))))
        print('Please enter another problem or type quit to exit.')

mainloop()
