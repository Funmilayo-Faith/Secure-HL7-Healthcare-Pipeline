import hashlib
def calculate_hash(file_path):
    """
    Calculates the SHA-256 hash of  file.
    """

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

hash_value = calculate_hash("encrypted_hl7_messages.txt")
print("\nSHA-256 Hash:\n")
print(hash_value)

with open(
    "encrypted_hash.txt",
    "w"
) as file:
    file.write(hash_value)

print("\nHash saved successfully.")