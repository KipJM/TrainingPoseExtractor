import os

def get_all_files(FILE_PATH):
    # Find all folders
    subfolders = []
    for root, dirs, files in os.walk(FILE_PATH):
        subfolders = dirs
        break

    file_paths = []

    for folder in subfolders:
        # Ignore .git files
        if folder[0] == '.':
            continue
        folder_path = os.path.join(FILE_PATH, folder)
        print(f'*SEARCHING {folder_path}')

        for root, dirs, files in os.walk(folder_path):
            print(files)
            for file in files:
                # ignore pose files
                if file.endswith('.pose'):
                    continue
                file_path = os.path.join(folder_path, file)
                file_paths.append(file_path)

    return file_paths
