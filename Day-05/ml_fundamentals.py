# DAY 5 - MACHINE LEARNING FUNDAMENTALS

# Import the Iris dataset
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()

# Separate features and target
X = iris.data
y = iris.target

# Display dataset information
print("MACHINE LEARNING - IRIS DATASET")

print("\nFEATURE NAMES:")
print(iris.feature_names)

print("\nTARGET NAMES:")
print(iris.target_names)

print("\nFEATURE DATA:")
print(X[:5])

print("\nTARGET DATA:")
print(y[:5])

print("\nDATASET SHAPE:")
print(X.shape)

print("\nTARGET SHAPE:")
print(y.shape)

print("\nTOTAL FLOWER SAMPLES:")
print(len(X))
