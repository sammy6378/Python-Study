import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
file_path = 'dataset.data'  # Replace with the correct file path if needed

# Define column names based on the dataset
column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

try:
    # Load the dataset with the specified column names
    data = pd.read_csv(file_path, header=None, names=column_names)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Ensure the dataset is in the correct location.")
    data = None

# Step 2: Inspect the dataset if loaded successfully
if data is not None:
    print("\nFirst 5 rows of the dataset:")
    print(data.head())

    # Step 3: Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())

    # Step 4: Summary Statistics
    print("\nSummary Statistics:")
    print(data.describe())

    # Step 5: Data Visualization

    # Histogram for Sepal Length
    plt.figure(figsize=(8, 6))
    plt.hist(data['SepalLength'], bins=20, color='blue', alpha=0.7)
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter Plot: Sepal Length vs Petal Length
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='SepalLength', y='PetalLength', hue='Species', data=data)
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    plt.legend(title='Species')
    plt.show()

    # Boxplot for Sepal Width across Species
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Species', y='SepalWidth', data=data)
    plt.title("Sepal Width by Species")
    plt.xlabel("Species")
    plt.ylabel("Sepal Width")
    plt.show()
