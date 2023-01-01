from random import randint, choice


# soring values and operations
def selecting_values(number_exs):
    
    values = list()
        
    for _ in range(number_exs):
        op = choice(['+', '-', '*', '/'])
        a = randint(1, 100)
        b = randint(1, 100)
        values.append((a, b, op)) 
        # adding a tuple with values and operations
                           
    return values


# printing the operation
def calculus(values): # enter a list with the values and operations
    
    answer = list()
    
    for a, b, op in values:
        result = float(input(f'{a} {op} {b} = '))
        answer.append((a, b, op, result)) # saving logs

    return answer # the original list with user's answers


# is it right?
def checking_answer(a, b, op, user_answer):
    right_answer = eval(f'{a}{op}{b}')
    right_answer = round(right_answer, 1)
    
    point = 1 if right_answer == user_answer else 0
    
    return point, right_answer
