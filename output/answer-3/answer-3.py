from numpy import fabs
import pandas as pd
d = pd.read_csv("./input/question-3/main.csv")
data = {'Team':d['Team'],
        'Yellow Cards':d['Yellow Cards'],
        'Red Cards':d['Red Cards']}
data=pd.DataFrame(data)
df = data.sort_values(by=['Red Cards','Yellow Cards'],ascending=False)
print(df)
df.to_csv("./output/answer-3/main.csv")