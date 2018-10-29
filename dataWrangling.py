#Problem Set 8
#Zachary Lyons
#INFO 3401 - INFO Exploration

#Collaboration between my usual table mates: Harold, Justin, Steven, Luke, and myself. 

import pandas as pd
import re
import csv

#Create function that takes .csv as input and outputs cleaned data
def generateCleanFile(input_file, clean_file):
    df = pd.read_csv(input_file, encoding='utf8', error_bad_lines=False, engine='python')
    
#noticed I was getting an error related to one specific line in the data. I used the error_bad_lines argument within the read_csv function to skip it, so it wouldn't continue breaking my entire program.

#Aaron recommended we start with #2
#Problem 2: Remove HTML tags
    df['comment_msg'] = df['comment_msg'].apply(lambda x: str(x).lstrip())
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'\r*',"", str(x)))
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'<.*?>',"",str(x)))

#Problem 1: Remove Spam
    remove_spam = ['app', 'free', '%20', 'check out my page', 'http://', 'www.', '.com']
    df = df[df.comment_msg.str.contains('|'.join(remove_spam)) == False]
    
#Problem 3: Remove null values
    df_no_nulls = df[pd.notnull(df['comment_msg'])]
    
#Export cleaned CSV
    df_no_nulls.to_csv(clean_file)

generateCleanFile("dd-comment-profile.csv", "cleaned_data.csv")