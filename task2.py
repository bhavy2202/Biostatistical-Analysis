import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/bhavyrahangdale/Downloads/B21006.xlsx', sheet_name='Task 2')

drug_A_freq_1 = df['S01'].to_numpy()
drug_A_freq_2 = df['S04'].to_numpy()
drug_A_freq_3 = df['S07'].to_numpy()
drug_B_freq_1 = df['S02'].to_numpy()
drug_B_freq_2 = df['S05'].to_numpy()
drug_B_freq_3 = df['S08'].to_numpy()
drug_C_freq_1 = df['S03'].to_numpy()
drug_C_freq_2 = df['S06'].to_numpy()
drug_C_freq_3 = df['S09'].to_numpy()

data = pd.DataFrame({
    'Inhibition': np.concatenate([drug_A_freq_1, drug_A_freq_2, drug_A_freq_3,
                                  drug_B_freq_1, drug_B_freq_2, drug_B_freq_3,
                                  drug_C_freq_1, drug_C_freq_2, drug_C_freq_3]),
    'Drug': np.repeat(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'], 15),
    'Frequency': np.tile(['1', '2', '3'], 45)
})

# Convert the Frequency column to categorical type
data['Frequency'] = pd.Categorical(data['Frequency'], categories=['1', '2', '3'], ordered=True)

# Perform two-way ANOVA
model = ols('Inhibition ~ C(Drug) + C(Frequency) + C(Drug):C(Frequency)', data=data).fit()
anova_table = sm.stats.anova_lm(model)

# Print the ANOVA table
print(anova_table)
F_ratio_drug = anova_table.loc['C(Drug)', 'F']
print(F_ratio_drug)
F_ratio_substance = anova_table.loc['C(Frequency)', 'F']
print(F_ratio_substance)
F_ratio_interaction = anova_table.loc['C(Drug):C(Frequency)', 'F']
print(F_ratio_interaction)

from scipy.stats import f
alpha = 0.05
critical_value_drug = f.ppf(1 - alpha, 2, 126)
print("critical_value_drug:", critical_value_drug)
critical_value_intake_freq = f.ppf(1 - alpha, 2, 126)
print("critical_value_intake_freq:", critical_value_intake_freq)
critical_value_intake_and_drug = f.ppf(1 - alpha, 4, 126)
print("critical_value_intake_and_drug:", critical_value_intake_and_drug)


# Box plots for main effects
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='Drug', y='Inhibition')
plt.xlabel('Drug')
plt.ylabel('Inhibition')
plt.title('Box Plot of Inhibition by Drug')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='Frequency', y='Inhibition')
plt.xlabel('Frequency')
plt.ylabel('Inhibition')
plt.title('Box Plot of Inhibition by Frequency')
plt.show()