import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings

# Filter out the warning message
warnings.filterwarnings("ignore", category=UserWarning)


# Load the Excel sheet into a pandas DataFrame
data = pd.read_excel('/Users/bhavyrahangdale/Downloads/B21006.xlsx', sheet_name='Task 3')

# Extract the columns of interest
C_level = data['C_level']
T_cell = data['T_cell']

# Reshape the data to match the input requirements of LinearRegression
C_level = C_level.values.reshape(-1, 1)
T_cell = T_cell.values.reshape(-1, 1)


# Create a Linear Regression model and fit the data
model = LinearRegression()
model.fit(C_level, T_cell)

# Predict the T cell counts based on the vitamin C levels
t_cell_predicted = model.predict(C_level)

# Plot the data and the linear regression line
plt.scatter(C_level, T_cell)
plt.plot(C_level, t_cell_predicted, color='red', linewidth=2)
plt.xlabel('Vitamin C Level (mcg/mm3)')
plt.ylabel('T Cell Count (cells/mm3)')
plt.title('Vitamin C Levels vs. T Cell Count')
plt.show()

# Get the coefficient and intercept of the linear regression line
coefficient = model.coef_[0][0]
intercept = model.intercept_[0]
print(f"Linear Regression Equation: T Cell Count = {coefficient:.2f} * Vitamin C Level + {intercept:.2f}")
