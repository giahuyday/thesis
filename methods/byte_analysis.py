import re

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

token = '0xdac17f958d2ee523a2206206994597c13d831ec7'


def hex_to_bytes(hex_string):
    hex_string = hex_string[2:] if hex_string.startswith("0x") else hex_string
    return bytes.fromhex(hex_string)


token_bytes = hex_to_bytes(token)
# print(token_bytes)


def read_file(file_path, token_bytes):
    free_bytes = []  # Save free byte array

    with open(file_path, 'rb') as f:
        bytes = f.read()
        # Traversal each byte
        for i, byte in enumerate(bytes):
            if byte == 0x00:  # Check if byte is free
                free_bytes.append((i, byte))  # save position and byte_value to free_byte array

    return free_bytes


# byte_string = b'\x00L\x00o\x00'
#
# # Chuyển mỗi byte thành chuỗi bit và nối chúng lại với nhau
bit_string = ''.join(format(byte, '08b') for byte in token_bytes)

# In chuỗi bit
print("Chuỗi bit:", bit_string)



folder_path = './'

file_list = os.listdir(folder_path)
b = [i for i in file_list if i.startswith('test')]


# Hàm để trích xuất số thứ tự từ tên tệp
def extract_number(file_name):
    match = re.search(r'\d+', file_name)
    return int(match.group()) if match else None


# Sắp xếp danh sách tên tệp theo số thứ tự
# sorted_file_names = sorted(b, key=extract_number)
# print(sorted_file_names)
# a = [[i, read_file(i, token_bytes)] for i in sorted_file_names]

# for i in range(len(sorted_file_names)):
# for i in a:
#     print(i[0])
#     print(i[1][:100])


