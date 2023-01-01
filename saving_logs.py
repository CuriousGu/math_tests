import pandas as pd 
from datetime import datetime


def append_log(df, accuracy, total_exercises):
    
    columns = ['+', '-', '*', '/', 'total_accuracy', 'total_exercises', 'date']
    values = df['operation'].value_counts().to_dict() # creating the dict with all the row's infos
   
    # adding the other infos to the same df, to convert it into a df
    values['total_accuracy'] = accuracy
    values['total_exercises'] = total_exercises
    values['date'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    df = pd.DataFrame(columns=columns, data=[values])
    return df


def adjusting_data(operation, user_answer, right_answer, df):
        
    if type(df) == bool:
        columns = ['operation', 'user_answer', 'right_answer']
        df = pd.DataFrame(columns=columns, data=[[operation, user_answer, right_answer]])
    else:
        novo_index = df.shape[0]
        df.loc[novo_index] = [operation, user_answer, right_answer]
        
    return df
