import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate sample data
np.random.seed(42)
data = {
    "Employee_ID": range(1, 1501),
    "Name": [fake.name() for _ in range(1500)],
    "Age": [np.random.choice([np.random.randint(18, 60), None], p=[0.9, 0.1]) for _ in range(1500)],
    "Department": [np.random.choice(["HR", "Finance", "IT", "hr", "finance", "it"]) for _ in range(1500)],
    "Salary": [np.random.choice([np.random.randint(30000, 120000), -1, None], p=[0.85, 0.05, 0.1]) for _ in range(1500)],
    "Joining_Date": [fake.date_between(start_date='-10y', end_date='today') for _ in range(1500)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv("employee_data.csv", index=False)
print("Sample dataset 'employee_data.csv' created!")