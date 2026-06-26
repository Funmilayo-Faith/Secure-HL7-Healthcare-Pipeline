from audit_logger import write_log
import hashlib
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()
current_hash = calculate_hash(
    "encrypted_hl7_messages.txt"
)
with open(
    "encrypted_hash.txt",
    "r"
) as file:
    saved_hash = file.read().strip()

if current_hash == saved_hash:
    print("\nIntegrity Check PASSED")
    print("No data tampering detected.")
else:
    print("\nIntegrity Check FAILED")
    print("WARNING: File has been modified!")
write_log(
    action="Integrity Check",
file_name="encrypted_hl7_messages.txt",
    records=100,
    status="PASSED"
    if current_hash == saved_hash
    else "FAILED"
)