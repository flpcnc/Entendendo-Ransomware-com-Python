import pyaes
import os
import sys

from file_handler import read_file, write_file, remove_file

file_name = "C:/Users/FLPCNC/Desktop/Ransomware/teste.txt.ransomwaretroll"
file_data = read_file(file_name)

os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

new_file_name = "teste.txt"
write_file(new_file_name, decrypt_data)
