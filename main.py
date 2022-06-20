import os


def run_fast_scandir(dir, ext):  # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files


path = input("Enter the directory to scan for your file: ")
file_ext = input("Enter the extension of the file you are searching for: ")
# file_ext = "." + file_ext
subfolders, files = run_fast_scandir(path, [file_ext])
print(files)