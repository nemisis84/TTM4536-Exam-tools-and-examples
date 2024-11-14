import requests
from bs4 import BeautifulSoup
import os

# The base URL for the hidden directory
base_url = "http://10.100.52.65:11632/.hidden/"

# Function to fetch all links from the given URL
def get_links_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href != '../':  # Skip parent directory links
            links.append(href)
    return links

# Function to recursively traverse directories and download README files
def traverse_and_download(url, download_dir):
    links = get_links_from_url(url)
    for link in links:
        if 'README' in link:  # If the link contains "README"
            print(f"Found README: {link} at {url}")
            response = requests.get(url + link)
            readme_number = ''.join(filter(str.isdigit, link))  # Extract number from README file name
            with open(os.path.join(download_dir, f"README{readme_number}"), 'w') as f:
                f.write(response.text)
        else:
            # Recursively follow directories
            traverse_and_download(url + link, download_dir)

# Function to merge README files in order
def merge_readme_files(download_dir, output_file):
    readme_files = [f for f in os.listdir(download_dir) if f.startswith('README')]
    readme_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))  # Sort by numeric value in file names
    with open(output_file, 'w') as outfile:
        for fname in readme_files:
            with open(os.path.join(download_dir, fname), 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n")  # Add a newline after each file content

# Main logic
def main():
    # Directory to store the downloaded README files
    download_dir = "readme_files"
    os.makedirs(download_dir, exist_ok=True)

    # Step 1: Download all README files
    traverse_and_download(base_url, download_dir)

    # Step 2: Merge all README files in order
    output_file = "merged_readme.txt"
    merge_readme_files(download_dir, output_file)
    print(f"Merged README files into {output_file}")

if __name__ == "__main__":
    main()
