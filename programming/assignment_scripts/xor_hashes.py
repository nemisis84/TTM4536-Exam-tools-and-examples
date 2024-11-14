def xor_hashes_with_prefix(file_path, prefix):
    xor_result = None

    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("Surname : "):
                # Extract the hash part of the line (after "Surname : ")
                hash_value = line.split(":")[1].strip()

                if hash_value.startswith(prefix):
                    # Convert the hash from hexadecimal to an integer
                    hash_int = int(hash_value, 16)
                    # print(hash_value)
                    # XOR all hash values together
                    if xor_result is None:
                        xor_result = hash_int
                    else:
                        xor_result ^= hash_int
                    # print(xor_result)
    
    xor_hex = hex(xor_result)[2:]  # Remove '0x' prefix
    xor_hex = xor_hex.zfill(64)  # Ensure it is 64 characters long (256-bit hash)

    # Debugging: Print filtered hashes and final result
    # print(f"Filtered hashes starting with {prefix}: {filtered_hashes}")
    print(f"FLAG10: {xor_hex}")
    return xor_result

# Path to the text file
file_path = "hashed_password_sql.txt"
# Prefix to filter hashes by (first two hex characters from Cookie tampering flag)
prefix = "ac"

# Call the function to XOR the hashes
result = xor_hashes_with_prefix(file_path, prefix)

# Print the final result (FLAG10)
if result is not None:
    print(f"FLAG10: {(hex(result))}")
else:
    print("No matching hashes found.")
