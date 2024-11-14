from langdetect import detect

# Function to check if the text is in English
def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

# Read and process the file
def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    current_id = None
    current_first_name = None

    for line in lines:
        # Detect and extract ID
        if line.startswith("Surname :"):
            current_id = line.split(":")[1].strip().split(" ")[0]

        # Detect and extract First name
        elif line.startswith("First name:"):
            current_first_name = line.split(":")[1].strip()

            # Check if the first name is in English
            if is_english(current_first_name):
                print(f"ID: {current_id}, First name: {current_first_name}")

# Example usage
process_file('SQLInjectioOutput.txt')

