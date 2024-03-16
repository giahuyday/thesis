import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math


def convert_s2bits(s):
    '''
    Chuyển chuỗi ký tự (ascii) thành list các bit.
    '''
    bits = []
    for c in s:
        c_bits = []
        for bit in list(bin(ord(c))[2:].zfill(8)):
            c_bits.append(int(bit))
        bits.extend(c_bits)
    return bits


def convert_bits2s(bits):
    '''
    Chuyển list các bit thành chuỗi ký tự (ascii).
    '''
    s = ''
    for i in range(0, len(bits), 8):
        c_bits = ''
        for bit in bits[i:i+8]:
            c_bits = c_bits + str(bit)
        c = chr(int(c_bits, 2))
        s = s + c
    return s


def euclidean_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2), color_avg(color2)


def color_avg(color):
    r,g,b = color
    if (r+g+b) % 2 == 1:
        return 1
    return 0


# Sort bảng màu
def minimum_position(palette):
    min = 9999
    position = 0
    for i in range(len(palette)):
        if round(palette[i][0], 7) < min and palette[i][0] != 0.0:
            min = palette[i][0]
            position = palette[i][2]
    return min, position


def pixel_position_update(color, palette, bits):
    sub_palette = []
    new_sub_palette = []

    for i in range(len(palette[0])):
      temp_palette, avg_color_i = euclidean_distance(color, palette[0][i])
      sub_palette.append([temp_palette, avg_color_i, i])

    for i in range(len(sub_palette)):
      # Kiểm tra xem sub_palette[i][1] có bằng bits hay không
      if sub_palette[i][1] == bits:
          # Nếu có, thêm phần tử này vào danh sách mới
          new_sub_palette.append(sub_palette[i])

    return new_sub_palette


def embed(msg_file, cover_img_file, stego_img_file):
    '''
    Fridrich sort image color palette methods.
    '''
    # Đọc cover img file
    cover_img = Image.open(cover_img_file)
    # plt.imshow(cover_img)
    cover_pixels = np.array(cover_img)
    plt.imshow(cover_img)
    palette = cover_img.getpalette() # Kết quả là list các giá trị Red, Green, Blue của các màu
                                     # trong bảng màu, 3 giá trị liên tiếp ứng với một màu
    palette = np.array(palette, dtype=np.uint8).reshape(1, -1, 3)# Reshape lại dưới dạng ảnh RGB
    # print(cover_pixels)
    # plt.figure(); plt.yticks([]); plt.imshow(palette, aspect=20) # Uncomment để xem bảng màu

    temp_palette = [] # Bảng màu tạm thời
    sub_palette = [] # Lưu sort theo bit 0
    sub_palette_1 = [] # Lưu sort theo bit 1

    # print(len(sub_palette[0]))
    # print(palette[0][63], palette[0][114])
    # print(palette[0][124])
    # print(palette)
    #Tính khoảng cách euclidean  sort palette
    temp_color = [0,0,0]
    temp_value = 0

    while temp_value < len(palette[0]): #Tìm màu có giá trị gần nhất để sort lại

        # Tạo ra 2 bảng màu tương ứng với 2 loại bit của anh là 0, 1 để khi so sánh và xử lí bits thì sẽ thay đổi pixels 1 cách phù hợp
        temp_color = palette[0][temp_value]
        temp_palette = pixel_position_update(temp_color, palette, 1)
        min_val, min_pos = minimum_position(temp_palette) # Tìm khoảng cách gần nhất
        sub_palette_1.append(min_pos)

        temp_palette = pixel_position_update(temp_color, palette, 0)
        min_val, min_pos = minimum_position(temp_palette) # Tìm khoảng cách gần nhất
        sub_palette.append(min_pos)

        temp_value += 1 #Sang màu tiếp theo và thực hiện lại vòng lặp

    # print(palette)
    # print(sub_palette_1)
    # print(sub_palette)

    # Đọc dữ liệu từ tệp tin
    s = msg_file

    # Chuyển đổi mảng s thành mảng 512x512 xem nhưng cắt bỏ phần bit dư so với số pixel tối đa 512x512 của ảnh
    s = np.array(s)
    s = np.resize(s, (512, 512))
    # print(s)
    # print(len(cover_pixels))
    # print(len(cover_pixels[0]))
    new_array = [(i, color_avg(i)) for i in palette[0]]

    for i in range(512):
        for j in range(512):
            if color_avg(palette[0][cover_pixels[i][j]]) != s[i][j]:
                # print(color_avg(palette[0][cover_pixels[i][j]]), s[i][j], i, j)
                if s[i][j] == 1:  # Kiểm tra giá trị của s[k]
                    cover_pixels[i][j] = sub_palette_1[cover_pixels[i][j]]
                else:
                    cover_pixels[i][j] = sub_palette[cover_pixels[i][j]]
            else:
                pass
    # print(cover_pixels[12])

    # Ghi stego pixels cùng palette xuống file
    stego_img = Image.fromarray(cover_pixels)
    stego_img.putpalette(cover_img.getpalette())
    stego_img.save(stego_img_file)


str = [i for i in '1101101011000001011111111001010110001101001011101110010100100011101000100010000001100010000001101001100101000101100101111100000100111101100000110001111011000111']
print(str)
embed(str, 'sample_file/lena.gif', 'encrypt_result/etest7.gif')
