import difflib
import sys

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def compare_files(file1_path, file2_path):
    file1_content = read_file_content(file1_path)
    file2_content = read_file_content(file2_path)

    diff = difflib.unified_diff(file1_content, file2_content, fromfile=file1_path, tofile=file2_path)

    for line in diff:
        print(line, end='')

if __name__ == "__main__":
    file1_path = input("Enter the path of the first file: ").strip()
    file2_path = input("Enter the path of the second file: ").strip()

    compare_files(file1_path, file2_path)
