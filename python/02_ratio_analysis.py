import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('/Users/afraaquil/Desktop/minor project/workforce_clean.csv')

print("Data loaded!")
print("Shape:", df.shape)
print("\nDepartments:", df['Department'].unique())

# Calculate average workload ratio per department
dept_wl = df.groupby('Department')['workload_ratio'].mean().reset_index()

# Calculate company average
company_avg = df['workload_ratio'].mean()

print("Company average workload ratio:", round(company_avg, 2))
print("\nDepartment workload:")
print(dept_wl)

# Flag each department as UNDERSTAFFED, BALANCED or OVERSTAFFED
dept_wl['status'] = dept_wl['workload_ratio'].apply(
    lambda x: 'UNDERSTAFFED' if x > company_avg * 1.05
    else ('OVERSTAFFED' if x < company_avg * 0.95
    else 'BALANCED'))

print("\nDepartment Status:")
print(dept_wl)
# Create bar chart
colors_map = {
    'UNDERSTAFFED': '#dc2626',   # red
    'BALANCED': '#16a34a',        # green
    'OVERSTAFFED': '#f59e0b'      # yellow
}

bar_colors = [colors_map[s] for s in dept_wl['status']]

plt.figure(figsize=(10, 5))
plt.bar(dept_wl['Department'], dept_wl['workload_ratio'], color=bar_colors)
plt.axhline(company_avg, color='blue', linestyle='--', label='Company Average')
plt.title('Workload Ratio by Department')
plt.xlabel('Department')
plt.ylabel('Avg Workload Ratio')
plt.legend()
plt.tight_layout()
plt.savefig('/Users/afraaquil/Desktop/minor project/workload_chart.png', dpi=150)
plt.show()
print("✅ Chart saved!")