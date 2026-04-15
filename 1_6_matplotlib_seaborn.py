import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Basic plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Line plot with multiple lines
y2 = [15, 25, 20, 35, 45]
plt.plot(x, y, label="Line 1", linestyle="--", marker="o")
plt.plot(x, y2, label="Line 2")
plt.title("Multiple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar plot
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]
plt.bar(categories, values, color=["red", "blue", "green", "orange"])
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color="purple", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
plt.scatter(x, y, color="cyan", edgecolor="black")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Seaborn heatmap
data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Seaborn Heatmap")
plt.show()

# Seaborn pairplot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.suptitle("Seaborn Pairplot", y=1.02)
plt.show()
