import numpy as np    # Import the NumPy library
import pandas as pd   # Import the Pandas library
import matplotlib.pyplot as plt   # Import the Matplotlib library
from sklearn.linear_model import LinearRegression   # Import the LinearRegression model from the sklearn library

# Read the shrink_ray_dataset.csv file into a Pandas DataFrame
dataSet = pd.read_csv("shrink_ray_dataset.csv")

# Extract the Power and Shrinkage columns from the DataFrame
x = dataSet[["Power"]]
y = dataSet[["Shrinkage"]]

# Create a LinearRegression model
regression = LinearRegression()

# Fit the model to the data
regression.fit(x, y)

# Generate predictions for the Shrinkage values
predict_y = regression.predict(x)

# Plot the actual Shrinkage values vs the predicted Shrinkage values
plt.scatter(x, y, color='red', label='Assembled')
plt.plot(x, predict_y, color='yellow', label='Predicted')

# Add labels and title to the plot
plt.title('Power VS Shrinkage')
plt.xlabel('Power')
plt.ylabel('Shrinkage')
plt.legend(loc="lower right")
plt.show()

# Calculate the specific value of x for which Shrinkage is 85
spec_x = (85 - regression.intercept_) / regression.coef_

# Print the specific value of x
print(spec_x)