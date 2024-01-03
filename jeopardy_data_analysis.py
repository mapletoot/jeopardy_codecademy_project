import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("jeopardy.csv")
print(df.head())

# Check column names
print(df.columns)

# Stripping columns of white space and converting to camel case
df.rename(columns = {"Show Number" : "show_id", " Air Date" : "date", " Round" : "round", " Category" : "category", " Value" : "value", " Question" : "question", " Answer" : "answer"}, inplace=True)
print(df.columns)


# queastion_searcher = lambda row: 



