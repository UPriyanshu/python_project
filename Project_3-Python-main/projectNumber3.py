import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Load the CSV file
file_path = "large_sales_data.csv"  # Ensure the file name matches your actual file
data = pd.read_csv(file_path, delimiter=";", usecols=["Month", "Sales"])

# Step 2: Data Preparation
# Convert sales to numeric (in case of bad data like strings)
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
data = data.dropna()  # Remove rows with NaN values

# Step 3: Perform Basic Data Analysis
mean_sales = np.mean(data["Sales"])  # Using numpy for mean
median_sales = np.median(data["Sales"])  # Using numpy for median

# Using scipy's mode function
mode_result = stats.mode(data["Sales"], keepdims=True)

# Check if the mode result contains any values and extract the mode
if mode_result.count[0] > 0:
    mode_sales = mode_result.mode[0]
else:
    mode_sales = None  # Handle case when there's no mode

# Step 4: Visualizing the Results (Bar Plot for Mean, Median, Mode)
analysis_results = {"Mean": mean_sales, "Median": median_sales, "Mode": mode_sales}

# Plotting the bar chart
plt.figure(figsize=(8, 6))
plt.bar(
    analysis_results.keys(),
    analysis_results.values(),
    color=["blue", "green", "orange"],
)

# Customizing the plot
plt.title("Basic Data Analysis of IoT Sales", fontsize=16)
plt.ylabel("Sales Value", fontsize=12)
plt.xlabel("Statistical Measure", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()

# Step 5: Print Basic Data Analysis Results
print("Basic Data Analysis Results:")
print(f"Mean Sales: {mean_sales:.2f}")
print(f"Median Sales: {median_sales:.2f}")
if mode_sales is not None:
    print(f"Mode Sales: {mode_sales:.2f}")
else:
    print("Mode Sales: No single mode found")
