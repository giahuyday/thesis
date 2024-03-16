from byte_analysis import hex_to_bytes

def embed_text_in_bytes(file_path, text):
    with open(file_path, 'rb') as f:
        data = bytearray(f.read())

    # Xác định vị trí của các byte trống (giá trị 0)
    empty_byte_indices = [i for i, byte in enumerate(data) if byte == 0x00]

    # Chuyển văn bản thành dạng byte
    text_bytes = hex_to_bytes(text)
    print(text_bytes)
    # Kiểm tra xem có đủ byte trống để nhúng văn bản không
    if len(text_bytes) > len(empty_byte_indices):
        print("Không đủ byte trống để nhúng văn bản.")
        return

    # # Nhúng văn bản vào các byte trống
    for i, byte in zip(empty_byte_indices[:len(text_bytes)], text_bytes):
        data[i] = byte
    #
    # # Ghi dữ liệu đã được cập nhật vào tệp
    with open('e'+file_path, 'wb') as f:
        f.write(data)


# Đường dẫn đến tệp
file_path = 'test27.pdf'

# Văn bản cần nhúng vào các byte trống
text_to_embed = "0xdac17f958d2ee523a2206206994597c13d831ec7"

# Nhúng văn bản vào các byte trống trong tệp
embed_text_in_bytes(file_path, text_to_embed)
