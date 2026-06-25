import pulp
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value, LpStatus

# --- Data based on our SQL query results ---
departments = ['Research & Development', 'Sales', 'Human Resources']

# Output gained per new hire (tasks per month from SQL Q4)
output_per_hire = {
    'Research & Development': 94,
    'Sales': 96,
    'Human Resources': 99
}

# Cost to hire one person per department
cost_per_hire = {
    'Research & Development': 7000,
    'Sales': 5000,
    'Human Resources': 3500
}

# Max hires allowed (based on headcount gap from Excel)
max_hires = {
    'Research & Development': 89,
    'Sales': 5,
    'Human Resources': 17
}

BUDGET = 500000

print("Data loaded!")
print(f"Budget: ${BUDGET:,}")

# --- Build the model ---
prob = LpProblem("Hiring_Optimization", LpMaximize)

# Decision variables — how many to hire in each department
hires = {d: LpVariable(f"hires_{d}", 
                        lowBound=0, 
                        upBound=max_hires[d], 
                        cat='Integer')
         for d in departments}

print("Decision variables created!")
print(hires)

# --- Objective: Maximize total output ---
prob += lpSum(output_per_hire[d] * hires[d] for d in departments)

# --- Constraint: Stay within budget ---
prob += lpSum(cost_per_hire[d] * hires[d] for d in departments) <= BUDGET

print("Objective and constraint added!")

# --- Solve the model ---
prob.solve(pulp.GLPK_CMD(msg=0))
print(f"\nStatus: {LpStatus[prob.status]}")
print(f"Max Output Gained: {value(prob.objective):.0f} tasks/month")
print(f"\nOptimal Hiring Plan:")
for d in departments:
    n = int(value(hires[d]))
    cost = cost_per_hire[d] * n
    print(f"  {d}: {n} hires → cost: ${cost:,}")

total_cost = sum(cost_per_hire[d] * int(value(hires[d])) for d in departments)
print(f"\nTotal Budget Used: ${total_cost:,}")
print(f"Budget Remaining: ${BUDGET - total_cost:,}")