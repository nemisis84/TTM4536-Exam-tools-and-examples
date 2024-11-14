import hashlib
import itertools
import string
import concurrent.futures

def sha256_hash(input_string):
    """Returns the SHA-256 hash of the input string."""
    return hashlib.sha256(input_string.encode()).hexdigest()

def find_matching_password(rightmost_8_chars, start_of_password = "simenmyr"):
    """Brute-force to find the correct password where the hash's last 8 characters match the given ones."""
    matching_passwords = []
    all_ascii_chars = string.ascii_letters + string.digits + string.punctuation 
    # + string.punctuation  # All possible characters

    wordlist = itertools.product(all_ascii_chars, repeat=5)

    filtered_combinations = itertools.dropwhile(lambda x: x[0] <= 'F', wordlist)
    # Generate all possible 5-character combinations
    for combination in filtered_combinations:
        # random_chars = start_of_password + ''.join(combination)
        random_chars = ''.join(combination)
        # Calculate the SHA-256 hash
        hash_value = sha256_hash(random_chars)
        # print(f"Trying: {random_chars}. with hash: {hash_value}")
        # Check if the last 8 characters of the hash match
        if hash_value[-8:] == rightmost_8_chars:
            matching_passwords.append((random_chars, hash_value))
            print(f"Found matching password: {random_chars}. with hash: {hash_value}")

    return matching_passwords

# Set the rightmost 8 characters of the Flag07 hash (as provided by the task)
rightmost_8_chars = "6f7fb26d"  # Replace this with the actual 8 characters from Flag07

# Find the password and corresponding hash
matching_passwords = find_matching_password(rightmost_8_chars)

# Output the results
print(f"Matching passwords: {matching_passwords}")
