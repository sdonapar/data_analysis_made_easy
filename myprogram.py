import os

files = os.listdir(".")
for file_name in files:
    if file_name.endswith("csv"):
        print file_name 