import pandas as pd
# Read the dataset
df = pd.read_csv("Mock_Haematology_Data.csv")

def create_hl7_message(patient):
    msh = (
        "MSH|^~\\&|LAB_SYSTEM|HAEMATOLOGY_LAB|"
        "EHR_SYSTEM|HOSPITAL|20250625||ORU^R01|MSG001|P|2.5"
    )
    pid = (
        f"PID|1|{patient['Patient_ID']}|"
        f"{patient['Patient_Name']}|"
        f"{patient['Gender']}"
    )
    obr = "OBR|1|CBC"
    obx1 = (
        f"OBX|1|NM|HB|"
        f"{patient['Hb_g_dL']}g/dL"
    )
    obx2 = (
        f"OBX|2|NM|PCV|"
        f"{patient['PCV']}%"
    )
    obx3 = (
        f"OBX|3|NM|WBC|"
        f"{patient['WBC_x10^9_L']}x10^9/L"
    )
    obx4 = (
        f"OBX|4|NM|PLT|"
        f"{patient['Platelets_x10^9_L']}x10^9/L"
    )
    message = "\n".join([
        msh,
        pid,
        obr,
        obx1,
        obx2,
        obx3,
        obx4
    ])
    return message
# Store all HL7 messages
all_messages = []

# Generate HL7 for every patient
for _, patient in df.iterrows():

    hl7_message = create_hl7_message(patient)
    all_messages.append(hl7_message)

# Display first message
print(all_messages[0])

print("\nTotal HL7 Messages Generated:", len(all_messages))
# Save HL7 messages

with open(
    "hl7_messages.txt",
    "w",
    encoding="utf-8"
) as file:

     for message in all_messages:
         file.write(message)
         file.write(
             "\n\n-------------------\n\n"
         )
print(
    "HL7 messages saved succesfully!"
)