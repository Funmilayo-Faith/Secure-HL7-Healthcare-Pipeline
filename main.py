from faker import Faker
import pandas as pd
import random

# Create Faker object
fake = Faker()

# Empty list
patients = []

# Generate 100 patients
for i in range(1, 101):

    patient = {
        "Patient_ID": f"P{i:04d}",
        "Patient_Name": fake.name(),
        "Gender": random.choice(["Male", "Female"]),
        "Hb_g_dL": round(random.uniform(8.0, 17.5), 1),
        "PCV": round(random.uniform(25.0, 52.0), 1),
        "WBC_x10^9_L": round(random.uniform(4.0, 11.0), 1),
        "Platelets_x10^9_L": random.randint(150, 400)
    }
    patients.append(patient)
# Convert to dataframe
df = pd.DataFrame(patients)

# Show first 10 records
print(df.head(10))

# Save CSV
df.to_csv(
    "Mock_Haematology_Data.csv", 
    index=False
)
print(
    "\n100 patients record saved sucessfully!"
)