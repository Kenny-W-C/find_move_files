import os

path = input("Enter the directory to scan: ")

filenames = next(os.walk(path), (None, None, []))[2]
print(filenames)
'''
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            for entry2 in os.scandir(os.path.join(path, entry)):
                print(entry2.name)
                if not entry.name.startswith('.') and entry.is_dir():
                    for entry2 in os.scandir(os.path.join(path, entry)):
                        print(entry2.name)
        else:
            print(entry.name)
'''