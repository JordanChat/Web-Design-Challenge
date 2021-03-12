import pandas as pandas
df = pandas.read_csv('Resources/cities.csv')
df.to_html('cities.html', index=False)
