import os

def read_file(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()
    return file_data

def write_file(file_name, data):
    with open(file_name, "wb") as file:
        file.write(data)

def remove_file(file_name):
    os.remove(file_name)
