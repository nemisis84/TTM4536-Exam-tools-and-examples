import hashlib
import random
import time

# Function to generate possible passwords
def generate_wordlist(password_file, output_file):
    # Read the passwords from the file
    with open(password_file, 'r') as file:
        pswdlist = [line.strip() for line in file.readlines()]
    
    # Open the output file to store the wordlist
    with open(output_file, 'w') as outfile:
        length = len(pswdlist)
        
        # Generate combinations of passwords
        for i in range(length):
            for j in range(length):
                pw1 = pswdlist[i]
                pw2 = pswdlist[j]
                pswd = pw1 + pw2
                
                # Compute md5 hash
                qq = hashlib.md5(pswd.encode()).hexdigest()
                
                # Write the password and its hash to the file
                outfile.write(f"{qq}\n{pswd}\n")

# Parameters
password_file = 'xato-net-10-million-passwords-second-1000s.txt'
output_file = 'generated_wordlist.txt'

# Call the function to generate the wordlist
generate_wordlist(password_file, output_file)

print(f"Wordlist generated and saved to {output_file}")
