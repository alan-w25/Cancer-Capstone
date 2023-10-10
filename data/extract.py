import requests
import csv
import tarfile
import os
import bz2

def download_and_extract_urls_from_manifest(file_path, target_directory):
    # Ensure target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # List to store URLs
    urls = []

    # Read the manifest file and extract URLs
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row
        for row in reader:
            urls.append(row[3])  # URLs are in the 4th column (0-indexed)

    # Download each URL
    for url in urls:
        filename = url.split('/')[-1]  # Take the last part of the URL as filename
        filepath = os.path.join(target_directory, filename)

        with open(filepath, 'wb') as file:
            file.write(requests.get(url).content)
        print(f"Downloaded {url} to {filepath}")

        # Extract the file based on its extension
        if filename.endswith('.tar.bz2'):
            with tarfile.open(filepath, 'r:bz2') as tar:
                extract_path = os.path.join(target_directory, os.path.splitext(filename)[0])
                tar.extractall(path=extract_path)
            print(f"Extracted contents of {filepath}")

        elif filename.endswith('.txt.bz2'):
            with bz2.BZ2File(filepath, 'rb') as f_in:
                decompressed_file = os.path.join(target_directory, os.path.splitext(filename)[0])  # remove .bz2 extension
                with open(decompressed_file, 'wb') as f_out:
                    f_out.write(f_in.read())
            print(f"Decompressed {filepath} to {decompressed_file}")

# Usage
manifest_path = "hmp_buccal_male.tsv"
target_dir = "m/"
download_and_extract_urls_from_manifest(manifest_path, target_dir)
