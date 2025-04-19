import pandas as pd
import plotly.express as px
import numpy as np

# Dataset
data = {
    'Diet': ['Vegans', 'Vegetarians', 'Fish-eaters', 'Low meat-eaters', 'Medium meat-eaters', 'High meat-eaters'] * 5,
    'Environmental Factor': ['GHG'] * 6 + ['Land'] * 6 + ['Water'] * 6 + ['Eutrophication'] * 6 + ['Biodiversity'] * 6,
    'Impact': [2.47, 4.16, 4.74, 5.37, 7.04, 10.24,
              4.37, 6.01, 6.31, 8.31, 11.28, 16.78,
              0.41, 0.53, 0.71, 0.71, 0.78, 0.89,
              10.70, 17.27, 21.09, 23.55, 29.61, 40.80,
              1.12, 2.08, 2.10, 2.29, 2.77, 3.69]
}

df = pd.DataFrame(data)

# Data Cleaning
# 1. Check for missing values
print("Number of missing values:")
print(df.isnull().sum())

# 2. Handle outliers (assuming Impact values cannot be negative)
df = df[df['Impact'] >= 0]

# 3. Ensure correct data types
df['Diet'] = df['Diet'].astype('category')
df['Environmental Factor'] = df['Environmental Factor'].astype('category')
df['Impact'] = df['Impact'].astype('float64')

# Create Treemap
fig = px.treemap(df,
                 path=['Environmental Factor', 'Diet'],
                 values='Impact',
                 color='Impact',
                 color_continuous_scale='RdYlGn',
                 title='Environmental Impact by Diet and Factor')

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig.show()