import numpy as np
import pandas as pd
import json

from bokeh.palettes import tol
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, DatetimeTickFormatter

#Load CSV file into Pandas dataframe
df = pd.read_csv('testdata.csv')

#Add day on to Month/Year column to format for datetime conversion
df['Month/Year'] = df['Month/Year'].apply(lambda x : '01/'+x)
#Convert to datetime
df['Month/Year'] = pd.to_datetime(df['Month/Year'], dayfirst=True)
source = ColumnDataSource(df)
source.data['x_values'] = [1,2,3,4,5,6,7,8,9,10,11,12]
p = figure(title='Report of Chief  Sanitary Inspector', x_axis_label='Date', y_axis_label='Count', x_axis_type='datetime')
p.line(x='Month/Year', y='Alleys Filthy', legend_label='Alleys Filthy', source=source)
p.line(x='Month/Year', y='Garbage and Filth Thrown on Vacant Lots', legend_label='Garbage and Filth Thrown on Vacant Lots', line_color="tomato", source=source)
p.legend.title = "Monthly Returns"
p.xaxis.formatter=DatetimeTickFormatter(hours="%d %B %Y",
days="%d %B %Y",
months="%d %B %Y",
years="%d %B %Y",
)
output_file('bokeh_plot.html')
show(p)
