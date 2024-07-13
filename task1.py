import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files based on their extensions.")
    parser.add_argument('source', type=str, help='Path to the source directory')
    parser.add_argument('destination', type=str, nargs='?', default='dist', help='Path to the destination directory (default: dist)')
    return parser.parse_args()

def copy_and_sort_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for root, _, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lstrip('.').lower() or 'no_extension'
            dest_dir = os.path.join(destination, file_extension)
            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            dest_file_path = os.path.join(dest_dir, file)
            try:
                shutil.copy2(file_path, dest_file_path)
                print(f'Copied: {file_path} -> {dest_file_path}')
            except Exception as e:
                print(f'Error copying {file_path} to {dest_file_path}: {e}')

def main():
    args = parse_arguments()
    source_dir = args.source
    destination_dir = args.destination

    if not os.path.exists(source_dir):
        print(f'Source directory {source_dir} does not exist.')
        return
    
    try:
        copy_and_sort_files(source_dir, destination_dir)
    except Exception as e:
        print(f'Error during processing: {e}')

if __name__ == "__main__":
    main()
