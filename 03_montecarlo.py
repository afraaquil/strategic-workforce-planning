import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed — makes results reproducible
np.random.seed(42)

simulations = 1000
target_hires = 20

print("Starting Monte Carlo Simulation...")
print(f"Target hires: {target_hires}")
print(f"Simulations: {simulations}")

# Run 1000 simulations
results = []

for i in range(simulations):
    # Random values for each scenario
    acceptance_rate = np.random.uniform(0.60, 0.90)
    cost_per_hire = np.random.uniform(3000, 8000)
    time_to_hire = np.random.randint(30, 90)
    
    # Calculate outcomes
    hires_made = int(target_hires * acceptance_rate)
    total_cost = hires_made * cost_per_hire
    
    # Store result
    results.append({
        'hires': hires_made,
        'cost': total_cost,
        'days': time_to_hire
    })

# Convert to DataFrame
res_df = pd.DataFrame(results)

print("\nSimulation complete!")
print(f"Avg hires made: {res_df['hires'].mean():.1f}")
print(f"Avg total cost: ${res_df['cost'].mean():,.0f}")
print(f"P(>=15 hires): {(res_df['hires']>=15).mean()*100:.1f}%")

# Create two charts side by side
plt.figure(figsize=(10, 4))

# Chart 1 — Distribution of hires
plt.subplot(1, 2, 1)
plt.hist(res_df['hires'], bins=15, color='#2563eb', edgecolor='white')
plt.title('Distribution of Hires Made')
plt.xlabel('Number of Hires')
plt.ylabel('Frequency')

# Chart 2 — Distribution of cost
plt.subplot(1, 2, 2)
plt.hist(res_df['cost']/1000, bins=15, color='#7c3aed', edgecolor='white')
plt.title('Distribution of Total Cost')
plt.xlabel('Cost ($000s)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('/Users/afraaquil/Desktop/minor project/montecarlo_chart.png', dpi=150)
plt.show()
print("✅ Monte Carlo chart saved!")