import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("jeopardy.csv")
print(df.head())
print(df.info())

# Check column names
print(df.columns)


# Stripping columns of white space and converting to camel case
df.columns = ["show_id", "date", "round", "category", "value_dollars", "question", "answer"]
# For the above line, it's also possible to do this: df.rename(columns = {"Show Number" : "show_id", " Air Date" : "date", " Round" : "round", " Category" : "category", " Value" : "value", " Question" : "question", " Answer" : "answer"}, inplace=True)

# Checking renaming has worked:
print(df.columns)

# Changing all the value_dollars to floats without '$' and ','
df.value_dollars = df.value_dollars.apply(lambda x: float(x[1:].replace(',', '')) if type(x) == str else 0)
print(df.value_dollars.mean())

# queastion_searcher = lambda row: 



