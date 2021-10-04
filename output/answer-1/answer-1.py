import pandas as pd
df1 = pd.read_csv("./input/question-1/main.csv")
data = {
         'Year':(df1['Year']//10)*10,
         'Population':df1['Population'],
         'Violent':df1['Violent'],
         'Property':df1['Property'],
         'Murder':df1['Murder'],
         'Forcible_Rape':df1['Forcible_Rape'],
         'Robbery':df1['Robbery'],
         'Aggravated_assault':df1['Aggravated_assault'],
         'Burglary':df1['Burglary'],
         'Larceny_Theft':df1['Larceny_Theft'],
         'Vehicle_Theft':df1['Vehicle_Theft']
         }
data=pd.DataFrame(data)
df2=data.groupby('Year').sum()
print(df2)
df2.to_csv("./output/answer-1/main.csv")