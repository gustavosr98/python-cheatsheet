# Write
with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)

# Read
with open('data.txt', 'r') as f:
    data = f.read()

# Directories
import os
with os.scandir('./') as entries:
    for entry in entries:
        print(entry.name)