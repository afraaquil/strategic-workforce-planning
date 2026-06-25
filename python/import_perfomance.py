import pandas as pd
import mysql.connector

df = pd.read_csv('/Users/afraaquil/Desktop/minor project/hr perfomance.csv')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Aiza@321',
    database='workforce_db'
)

cursor = conn.cursor()
count = 0

for _, row in df.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO performance 
        (emp_id, performance_score, tasks_completed, 
         contract_hours, training_hours, skill_rating)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        int(row['EmployeeNumber']),
        int(row['PerformanceScore']),
        int(row['TasksCompleted']),
        int(row['ContractHours']),
        int(row['TrainingHours']),
        int(row['SkillRating'])
    ))
    count += 1

conn.commit()
print(f"✅ Done! {count} rows inserted")
cursor.close()
conn.close()