import pandas as pd
import plotly.express as px
data = [1,2,3]
df = pd.read_csv('Covid.csv')
print(df)
fig = px.scatter(df,x = 'date', y = 'cases', color = 'country')
fig.show()
