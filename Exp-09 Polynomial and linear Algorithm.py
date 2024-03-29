import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([2, 5, 9, 15, 21, 28, 35])

# Perform linear regression
linear_coefficients = np.polyfit(x, y, 1)
linear_regression = np.poly1d(linear_coefficients)

# Perform polynomial regression with degree 2
polynomial_coefficients = np.polyfit(x, y, 2)
polynomial_regression = np.poly1d(polynomial_coefficients)

# Generate data for the regression lines
x_fit = np.linspace(0, 8, 100)
linear_y_fit = linear_regression(x_fit)
polynomial_y_fit = polynomial_regression(x_fit)

# Plot the original data and regression lines
plt.scatter(x, y, label='Original Data')
plt.plot(x_fit, linear_y_fit, label='Linear Regression', linestyle='dashed')
plt.plot(x_fit, polynomial_y_fit, label='Polynomial Regression (degree 2)', linestyle='dotted')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Comparison of Polynomial and Linear Regression')
plt.grid(True)
plt.show()