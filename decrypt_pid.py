from audit_logger import write_log
from cryptography.fernet import Fernet
# ================
# LOAD ENCRYPTION KEY
# ================

with open("secret.key", "rb") as key_file:
    key = key_file.read()
cipher = Fernet(key)

# ================
# READ ENCRYPTION FILE
# ================

with open(
    "encrypted_hl7_messages.txt",
    "r",
    encoding="utf-8"
) as file:
    encrypted_content = file.read()
# ================
# DEBUG CHECK
# ================
print("\nLAST 5 LINES OF ENCRYPTED FILE:\n")

for line in encrypted_content.splitlines()[-5:]:
    print(repr(line)) 

# =================
# DECRYPT PID SEGMENTS
# =================
decrypted_lines = []
decrypted_count = 0
for line in encrypted_content.splitlines():

    if line.startswith("PID_ENCRYPTED|"):
        decrypted_count += 1
        encrypted_pid = line.replace(
            "PID_ENCRYPTED|",
            "",
            1
        )
        decrypted_pid = cipher.decrypt(
            encrypted_pid.encode()
        ).decode()
       
        decrypted_lines.append(
            decrypted_pid
        )
    else:  
        decrypted_lines.append(
        line
    )

# ==============
# SAVE DECRYPTED FILE
# ==============
with open(
    "decrypted_hl7_messages.txt",
    "w",
    encoding="utf-8"
) as file:
    
    file.write(
        "\n".join(decrypted_lines)
    )
# =====================
# SUCCESS MESSAGE
# =====================

print("\nDecrypted HL7 file saved successfully!"
)
print(
    f"PID segments decrypted:{decrypted_count}"
)
print(
   f"Number of lines in decrypted file:{len(decrypted_lines)}"
)
write_log(
    action="PID_Decryption",
file_name="decrypted_hl7_messages.txt",
    records=decrypted_count,
    status="SUCCESS"
)