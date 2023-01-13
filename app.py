from tests import selecting_values, calculus, checking_answer
from saving_logs import append_log, adjusting_data
import os 
import time 

def main():
    
    # beggining 
    number_exs = int(input('How many exercises would you like to do?  '))
    os.system("clear")

    points = 0 
    values = selecting_values(number_exs)
    
    init = time.time() # when the calculation starts
    answer = calculus(values)
    end = time.time() # when the calculation ends
    
    logs = False 
    
    # cleaning to show the accuracy and the right answers
    os.system('clear')
    
    # test time
    test_duration = end - init
    test_duration = time.strftime("%Mmin %Ss", time.gmtime(test_duration)) # formating the time
    
    for a, b, op, user_answer in answer:
        result, right_answer = checking_answer(a, b, op, user_answer)
        points += result
        print(f'{a} {op} {b} = {right_answer}\nSua resposta: {user_answer}', end='\n\n') # showing the correct answer
        logs = adjusting_data(op, user_answer, right_answer, logs) # saving all the logs
        
    accuracy = round(points/len(values), 2)*100
    print(f'Acurácia --> {accuracy}% ')
    print(f'Tempo -->  {test_duration}')
    
    df = append_log(logs, accuracy, len(values),test_duration) # formating df 
    df.to_csv('logs.csv', mode='a', index=False) # savng df in csv
    
    
if __name__ == "__main__":
    main()
    