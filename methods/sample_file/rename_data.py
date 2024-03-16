import os

# Đường dẫn đến thư mục chứa các tệp
folder_path = './'

# Lấy danh sách các tệp trong thư mục
file_list = os.listdir(folder_path)
print(file_list)
# Duyệt qua từng tệp trong danh sách
for old_name, i in zip(file_list, range(len(file_list))):
    # Tạo đường dẫn tới tệp cũ
    old_path = os.path.join(folder_path, old_name)

    # Tạo tên mới dựa trên tên tệp cũ (ở đây chỉ là ví dụ, bạn có thể thay đổi cách đặt tên tùy ý)
    new_name = old_name.replace('file (1)', f'test{i}')

    # Tạo đường dẫn tới tệp mới
    new_path = os.path.join(folder_path, new_name)

    # Đổi tên tệp
    os.rename(old_path, new_path)

    # In ra thông báo sau khi đổi tên
    print(f"Đã đổi tên '{old_name}' thành '{new_name}'")