# Hướng dẫn tạo chạy và cài đặt.

### Chạy câu lệnh để download các thư viện cần thiết
```shell    
pip3 install -r requirements.txt
```

### Câu lệnh test methods water marking trên ubuntu
```shell
python3 main.py 'water_mark_infor' './methods/test1.pdf'
```

### Câu lệnh test methods water marking trên window theo file path
```shell
python3 main.py 'water_mark_infor' 'methods\test1.pdf'
```

### Câu lệnh test methods thêm token vào trailer của file pdf
```shell
python3 ./methods/trailer_processor.py
```

### Câu lệnh test methods thêm token vào trailer của file pdf cho window file path
```shell
python ./methods/trailer_processor.py
```
