import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the dataset from Excel
data = pd.read_excel('/Users/bhavyrahangdale/Downloads/B21006.xlsx', sheet_name='Task 1')

# Drop rows with missing values
data = data.dropna()

# Extract the data from the 'Diet' and 'Control' columns
group1 = data['Diet']
group2 = data['Control']

# Perform independent samples t-test
t_statistic, p_value = ttest_ind(group1, group2)

# Calculate descriptive statistics
group1_mean = group1.mean()
group2_mean = group2.mean()
group1_std = group1.std()
group2_std = group2.std()

# Create a figure with subplots for box plot and bar plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Box plot
sns.boxplot(data=[group1, group2], palette=["lightblue", "lightgreen"], ax=ax1)
ax1.set_xlabel("Group")
ax1.set_ylabel("Iron Concentration (mcg/L)")
ax1.set_title("Comparison of Iron Concentration in Diet vs. Control Groups")
ax1.set_xticks(ticks=[0, 1])
ax1.set_xticklabels(["Diet", "Control"])

# Bar plot
sns.barplot(x=["Diet", "Control"], y=[group1_mean, group2_mean], palette=["lightblue", "lightgreen"], ax=ax2)
ax2.set_xlabel("Group")
ax2.set_ylabel("Mean Iron Concentration (mcg/L)")
ax2.set_title("Mean Iron Concentration in Diet vs. Control Groups")

# Add error bars representing standard deviation
ax2.errorbar(x=["Diet", "Control"], y=[group1_mean, group2_mean], yerr=[group1_std, group2_std], fmt='none', ecolor='black')

# Show the plots
plt.tight_layout()
plt.show()

# Generate statistical analysis report
print("\nStatistical Analysis Report:")
print("The independent samples t-test assesses whether the observed difference in mean iron concentration between the 'Diet' and 'Control' groups is statistically significant.")
print("Null Hypothesis (H0): There is no significant difference in the mean iron concentration between the groups.")
print("Alternative Hypothesis (Ha): There is a significant difference in the mean iron concentration between the groups.")
print("t-statistic:", t_statistic)
print("p-value:", p_value)
print("Group 1 Mean:", group1_mean)
print("Group 2 Mean:", group2_mean)
print("Group 1 Standard Deviation:", group1_std)
print("Group 2 Standard Deviation:", group2_std)
