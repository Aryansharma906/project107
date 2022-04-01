import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import csv 
import statistics


data = pd.read_csv('data.csv')
# student_data = data.loc[data['student_id'] == 'TRL_xsl']

print(data.groupby('level')['attempt'].mean())

fig = px.scatter(data, x ='student_id', y ='level', color ='attempt', size ='attempt' )
fig.show()


