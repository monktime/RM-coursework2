import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample historical dietary consumption data (year, GHG emissions in million tons)
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'GHG_Emissions': [30, 32, 31, 35, 34, 36, 38, 42, 41, 43]  # Sample emissions data
}

# Create a DataFrame
df = pd.DataFrame(data)

# Prepare the data for modeling
X = df[['Year']]  # Feature variable
y = df['GHG_Emissions']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future emissions for the next 10 years
future_years = np.arange(2020, 2030).reshape(-1, 1)
predictions = model.predict(future_years)

# Combine historical and future data for visualization
years_combined = np.concatenate((X['Year'].values, future_years.flatten()))
emissions_combined = np.concatenate((y.values, predictions))

# Plotting the results
plt.figure(figsize=(10, 5))
plt.scatter(X['Year'], y, color='blue', label='Historical Data')
plt.plot(years_combined, emissions_combined, color='orange', label='Predictions')
plt.xlabel('Year')
plt.ylabel('GHG Emissions (Million Tons)')
plt.title('Prediction of GHG Emissions Over the Next 10 Years')
plt.axvline(x=2019, color='red', linestyle='--', label='Prediction Start')
plt.legend()
plt.show()