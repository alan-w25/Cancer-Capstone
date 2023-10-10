import os

def delete_bz2_files(directory):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.bz2'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}. Reason: {e}")

# Usage
target_dir = "f/"
delete_bz2_files(target_dir)
