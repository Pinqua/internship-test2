import pandas as pd
df = pd.read_csv('./input/question-2/main.csv')
df=df.groupby('occupation').agg({'age':['min','max']})
print(df)
df.to_csv("./output/answer-2/main.csv")