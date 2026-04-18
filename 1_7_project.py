import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Inspect the dataset
print(titanic.info())
print(titanic.describe())

# Handle missing values
titanic["Age"].fillna(titanic["Age"].median())
titanic["Embarked"].fillna(titanic["Embarked"].mode()[0])

# Remove duplicates
titanic.drop_duplicates(inplace=True)

# Filter data: First-class passengers
first_class = titanic[titanic["Pclass"] == 1]
print(first_class.head())

# Bar chart of survival by class
survival_by_class = titanic.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color=["red", "blue", "green"])
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# Histogram of ages
plt.hist(titanic["Age"].dropna(), bins=30, color="purple", edgecolor="black")
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter plot of age vs fare
plt.scatter(titanic["Age"], titanic["Fare"], color="cyan", edgecolor="black")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()