from audit_logger import write_log
from cryptography.fernet import Fernet
# =================
# LOAD ENCRYPTION KEY
# =================

with open ("secret.key", "rb") as key_file:
    key = key_file.read()
cipher = Fernet(key)
print(key)
print(type(key))
print(len(key))

# =================
# READ HL7 FILE
# =================

with open(
    "hl7_messages.txt",
    "r",
    encoding="utf-8"
) as file:
    
    hl7_content = file.read()

# =================
# PROCESS EACH LINE
# =================

encrypted_lines = []
encrypted_count = 0

for line in hl7_content.splitlines():
    # Encrypt PID segments only
    if line.startswith("PID|"):
        encrypted_count += 1

        encrypted_pid = cipher.encrypt(line.encode()).decode()
        encrypted_lines.append(
            f"PID_ENCRYPTED|{encrypted_pid}")
    else:
        encrypted_lines.append(line)
# ==================
# SAVE SECURED FILE
# ==================

with open(
    "encrypted_hl7_messages.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(
        "\n".join(encrypted_lines)
    )

# ===============
# SUCCESS MESSAGE
# ===============
    
print("Encrypted HL7 file saved successfully!")
print(f"PID segments emcrypted: {encrypted_count}")

write_log(
    action="PID_Encryption",
file_name="encrypted_hl7_messages.txt",
    records=encrypted_count,
    status="SUCCESS"
)








