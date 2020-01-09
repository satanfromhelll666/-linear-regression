
# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datasets
 
datasets = pd.read_csv('Salary_Data.csv')

X = datasets.iloc[:, :-1].values
Y = datasets.iloc[:, 1].values

print("--------------------------------")
print("values of X")
print(X)
print("--------------------------------")
print("values of Y")
print(Y)

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 1/2, random_state = 0)

# Fitting Simple Linear Regression to the training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

# Predicting the Test set result ￼

Y_Pred = regressor.predict(X_Test)

print("--------------------------------")
print("values of X Tested")
print(X_Test)

print("--------------------------------")
print("values of Y prepered")
print(Y_Pred)

# Visualising the Test set results

plt.scatter(X_Test, Y_Test, color = 'green')
plt.plot(X_Test, regressor.predict(X_Test), color = 'blue')
plt.title('Salary vs Experience  (Training Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()


# Visualising the Training set results

plt.scatter(X_Train, Y_Train, color = 'red')
plt.plot(X_Train, regressor.predict(X_Train), color = 'blue')
plt.title('Salary vs Experience  (Original Set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

